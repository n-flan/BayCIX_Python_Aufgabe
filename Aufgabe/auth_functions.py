from custom_logger import logger
import smtplib

def auth_plain(smtp: smtplib.SMTP):    
    logger.info('Testing method PLAIN')
    try:
        smtp.auth('PLAIN', smtp.auth_plain)
        logger.info('Testing method PLAIN succeeded')
    except Exception as e:
        logger.error(f'Testing method PLAIN failed. Exception: {e}')

def auth_login(smtp: smtplib.SMTP):
    logger.info('Testing method LOGIN')
    try:
        smtp.auth('LOGIN', smtp.auth_login)
        logger.info('Testing method LOGIN succeeded')
    except Exception as e:
        logger.error(f'Testing method LOGIN failed. Exception: {e}')

def auth_cram_md5(smtp: smtplib.SMTP):
    logger.info('Testing method CRAM-MD5')
    try:
        smtp.auth('CRAM-MD5', smtp.auth_cram_md5)
        logger.info('Testing method CRAM-MD5 succeeded')
    except Exception as e:
        logger.error(f'Testing method CRAM-MD5 failed. Exception: {e}')