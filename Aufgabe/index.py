import yaml
from custom_logger import logger
from smtplib import SMTP
from auth_functions import auth_plain, auth_login, auth_cram_md5

# Import config file and set variables
with open('./Aufgabe/Config/config.yaml', 'r') as config:
   data = yaml.full_load(config)
   
smtp_server = data.get('smtp_server')
username = data.get('username')
password = data.get('password')

# Query user if they want to use a speciic port other than the default.
input_port = input("Enter port that should be used. If left empty, port 587 will be used as default: ")
config_port = data.get('port')

if len(input_port) == 0:
    port = config_port
else:
    port = input_port

# This function connects to a smtp server, activates TLS if necessary, and sets username and password.
def connect_smtp(smtp):
    smtp.connect(smtp_server,port)
    logger.debug(f'Connected with SMTP-Server: {smtp_server}')
    
    smtp.ehlo()
    if smtp.has_extn("STARTTLS"):
        logger.debug('Server supports TLS extension.')
        smtp.starttls()
        logger.debug('TLS activated.')
    else:
        logger.warning('Server does not support TLS extension!')
    smtp.ehlo()
    
    # Setting username and password AFTER activating TLS, if possible
    smtp.user = username
    smtp.password = password
    
# This function simpley disconnects from the server in order to be able to reauthenticate again.
def disconnect_smtp(smtp):
    smtp.close()
    logger.debug(f'SMTP-Server {smtp_server} disconnected.')
    
try:
    with SMTP(smtp_server,port) as smtp:
        # To view exact instructions that are sent to SMTP-server set debuglevel to 1
        smtp.set_debuglevel(0)
        
        connect_smtp(smtp)
        
        # Requesting supported auth methods which are return in a dictionary.
        supported_auth_methods = list(dict.fromkeys(smtp.esmtp_features.get("auth", "").split()))
              
        if supported_auth_methods:
            # Iterate through each supported authentication method to test functionality
            logger.info(f'Testing the following auth methods that were returned from SMTP server: {supported_auth_methods}')
            for auth_method in supported_auth_methods:
                match auth_method:
                    case 'PLAIN':
                        connect_smtp(smtp)
                        auth_plain(smtp)
                        disconnect_smtp(smtp)
                    case 'LOGIN':
                        connect_smtp(smtp)
                        auth_login(smtp)
                        disconnect_smtp(smtp)
                    case 'CRAM-MD5':
                        connect_smtp(smtp)
                        auth_cram_md5(smtp)
                        disconnect_smtp(smtp)
                        
                    # case 'DIGEST-MD5':
                    #     auth_digest_md5()
                    # case 'OAUTH':
                    #     auth_oauth()
                    # case 'GSSAPI':
                    #     auth_gssapi()
                    # case 'NTLM':
                    #     auth_ntlm()
        else:
            logger.warning(f'No auth methods are supported by this smtp server! Server ({smtp_server}) returned: {supported_auth_methods}')
except Exception as e:
    logger.error(f'Something went wrong | Exception: {e} ')
