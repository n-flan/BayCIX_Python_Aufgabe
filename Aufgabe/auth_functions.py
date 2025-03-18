from custom_logger import logger
import smtplib

def auth_plain(smtp: smtplib.SMTP):    
    smtp.connect()
    logger.info('Testing method PLAIN')
    try:
        smtp.auth('PLAIN', smtp.auth_plain)
        logger.info('Testing method PLAIN succeeded')
    except Exception as e:
        logger.error(f'Testing method PLAIN failed. Exception: {e}')
    smtp.close()

def auth_login(smtp: smtplib.SMTP):
    smtp.connect()
    logger.info('Testing method LOGIN')
    try:
        smtp.auth('LOGIN', smtp.auth_login)
        logger.info('Testing method LOGIN succeeded')
    except Exception as e:
        logger.error(f'Testing method LOGIN failed. Exception: {e}')
    smtp.close()

def auth_cram_md5(smtp: smtplib.SMTP):
    smtp.connect()
    logger.info('Testing method CRAM-MD5')
    try:
        smtp.auth('CRAM-MD5', smtp.auth_cram_md5)
        logger.info('Testing method CRAM-MD5 succeeded')
    except Exception as e:
        logger.error(f'Testing method CRAM-MD5 failed. Exception: {e}')
    smtp.close()

def auth_digest_md5():
    logger.info('Testing method DIGEST-MD5')
    print('This function is not implemented yet.')
    
def auth_oauth():
    logger.info('Testing method OAUTH')
    print('This function is not implemented yet.')
    
def auth_gssapi():
    logger.info('Testing method GSSAPI')
    print('This function is not implemented yet.')
    
def auth_ntlm():
    logger.info('Testing method NTLM')
    print('This function is not implemented yet.')