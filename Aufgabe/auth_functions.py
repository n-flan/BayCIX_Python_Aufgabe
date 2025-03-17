def auth_plain(smtp):    
    smtp.connect()
    response_plain = smtp.auth('PLAIN', smtp.auth_plain)
    print(response_plain)
    smtp.close()

def auth_login(smtp):
    smtp.connect()
    response_login = smtp.auth('LOGIN', smtp.auth_login)
    print(response_login)
    smtp.close()

def auth_cram_md5(smtp):
    smtp.connect()
    response_cram_md5 = smtp.auth('CRAM-MD5', smtp.auth_cram_md5)
    print(response_cram_md5)
    smtp.close()

def auth_digest_md5():
    print('This function is not implemented yet.')
    
def auth_oauth():
    print('This function is not implemented yet.')
    
def auth_gssapi():
    print('This function is not implemented yet.')
    
def auth_ntlm():
    print('This function is not implemented yet.')