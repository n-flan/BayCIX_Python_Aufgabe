import yaml
from smtplib import SMTP

# Import config file
with open('./Aufgabe/config.yaml', 'r') as config:
   data = yaml.full_load(config)

port = data.get('port')
smtp_server = data.get('smtp_server')
username = data.get('username')
password = data.get('password')

try:
    with SMTP(smtp_server, port) as smtp:
        # Setting username and password
        smtp.user = username
        smtp.password = password
        
        # TLS-Handshake and Ehlo
        smtp.starttls()
        smtp.ehlo()
        
except:
    print(f'Something went wrong while trying to establish a connection to the SMTP server! SMTP-Server: {smtp_server}, Port: {port} ')

#Requesting supported auth methods which are return in a dictionary.
supported_auth_methods = list(dict.fromkeys(smtp.esmtp_features.get("auth").split()))
print(f"Supported authentication methods: {supported_auth_methods}")

smtp.connect()
response_plain = smtp.auth('PLAIN',smtp.auth_plain)
print(response_plain)
smtp.close()

smtp.connect()
response_login = smtp.auth('LOGIN', smtp.auth_login)
print(response_login)
smtp.close()

smtp.connect()
response_cram_md5 = smtp.auth('CRAM-MD5', smtp.auth_cram_md5)
print(response_cram_md5)
smtp.close()

