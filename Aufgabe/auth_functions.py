import logging

logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG)

def auth_plain(smtp):    
    smtp.connect()
    logging.info('Testing method PLAIN')
    try:
        smtp.auth('PLAIN', smtp.auth_plain)
        logging.info('Testing method PLAIN succeeded')
    except:
        logging.error('Testing method PLAIN failed.')
    smtp.close()

def auth_login(smtp):
    smtp.connect()
    logging.info('Testing method LOGIN')
    try:
        smtp.auth('LOGIN', smtp.auth_login)
        logging.info('Testing method LOGIN succeeded')
    except:
        logging.error('Testing method LOGIN failed.')
    smtp.close()

def auth_cram_md5(smtp):
    smtp.connect()
    logging.info('Testing method CRAM-MD5')
    try:
        smtp.auth('CRAM-MD5', smtp.auth_cram_md5)
        logging.info('Testing method CRAM-MD5 succeeded')
    except:
        logging.error('Testing method CRAM-MD5 failed.')
    smtp.close()

def auth_digest_md5():
    logging.info('Testing method DIGEST-MD5')
    print('This function is not implemented yet.')
    
def auth_oauth():
    logging.info('Testing method OAUTH')
    print('This function is not implemented yet.')
    
def auth_gssapi():
    logging.info('Testing method GSSAPI')
    print('This function is not implemented yet.')
    
def auth_ntlm():
    logging.info('Testing method NTLM')
    print('This function is not implemented yet.')