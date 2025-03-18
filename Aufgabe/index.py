import yaml
from custom_logger import logger
from smtplib import SMTP
from auth_functions import auth_plain, auth_login, auth_cram_md5, auth_digest_md5, auth_oauth, auth_gssapi, auth_ntlm

# Import config file
with open('./Aufgabe/config.yaml', 'r') as config:
   data = yaml.full_load(config)

port = data.get('port')
smtp_server = data.get('smtp_server')
username = data.get('username')
password = data.get('password')

try:
    with SMTP(smtp_server, port) as smtp:
        
        smtp.set_debuglevel(1)
        
        logger.info(f'Connected with SMTP-Server: {smtp_server}')
        
        # Checking if server supports TLS
        smtp.ehlo()
        if smtp.has_extn("STARTTLS"):
            logger.info('Server supports TLS extension.')
            smtp.starttls()
            logger.info('TLS activated.')
        else:
            logger.warning('Server does not support TLS extension!')
            
        smtp.ehlo()    
            
        # Setting username and password AFTER activating TLS, if possible
        smtp.user = username
        smtp.password = password

        # Requesting supported auth methods which are return in a dictionary.
        supported_auth_methods = list(dict.fromkeys(smtp.esmtp_features.get("auth", "").split()))
        
        if supported_auth_methods:
            logger.info(f"Supported authentication methods: {supported_auth_methods}")

            # Iterate through each supported authentication method to test functionality
            logger.info(f'Testing the following auth methods that were returned from SMTP server: {supported_auth_methods}')
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
        else:
            logger.warning(f'No auth methods are supported by this smtp server! Servername: {smtp_server}')
except Exception as e:
    logger.error(f'Something went wrong | Exception: {e} ')
