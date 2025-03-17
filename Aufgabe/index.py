import yaml
from smtplib import SMTP

# Import config file
with open('./Aufgabe/config.yaml', 'r') as config:
   data = yaml.full_load(config)


port = data.get('port')
smtp_server = data.get('smtp_server')
username = data.get('username')
password = data.get('password')

print(port)
print(smtp_server)

smtpObj = SMTP(smtp_server, port)
