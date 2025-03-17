import yaml
import logging
from smtplib import SMTP
from auth_functions import auth_plain, auth_login, auth_cram_md5, auth_digest_md5, auth_oauth, auth_gssapi, auth_ntlm

logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG)

# Import config file
with open('./Aufgabe/config.yaml', 'r') as config:
   data = yaml.full_load(config)

port = data.get('port')
smtp_server = data.get('smtp_server')
username = data.get('username')
password = data.get('password')

try:
    with SMTP(smtp_server, port) as smtp:
        
        logging.info(f'Connected with SMTP-Server: {smtp_server}')
        
        # Setting username and password
        smtp.user = username
        smtp.password = password
        
        # TLS-Handshake and Ehlo
        smtp.starttls()
        smtp.ehlo()

        # Requesting supported auth methods which are return in a dictionary.
        supported_auth_methods = list(dict.fromkeys(smtp.esmtp_features.get("auth").split()))
        logging.info(f"Supported authentication methods: {supported_auth_methods}")

        # Iterate through each supported authentication method to test functionality
        logging.info(f'Testing the following auth methods that were returned from SMTP server: {supported_auth_methods}')
        for auth_method in supported_auth_methods:
            match auth_method:
                case 'PLAIN':
                    auth_plain(smtp)
                case 'LOGIN':
                    auth_login(smtp)
                case 'CRAM-MD5':
                    auth_cram_md5(smtp)
                case 'DIGEST-MD5':
                    auth_digest_md5()
                case 'OAUTH':
                    auth_oauth()
                case 'GSSAPI':
                    auth_gssapi()
                case 'NTLM':
                    auth_ntlm()

except:
    logging.error(f'Something went wrong while trying to establish a connection to the SMTP server! SMTP-Server: {smtp_server}, Port: {port} ')
