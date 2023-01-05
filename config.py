import random


first_name = 'Иван'
last_mame = 'Иванов'
valid_email = 'tobeve1988@dmtubes.com'
valid_password = '@cxLzXZBGE46gz7'
valid_telephone = '+***********'
no_valid_telephone = '+***********'
url_rostelecom = 'https://b2c.passport.rt.ru/'
start_web = 'https://start.rt.ru/'

url_cod = 'https://my.rt.ru/'
url_email = "temp-mail.org/ru/"

engl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
domens = ['com','ua','ru','net']

def pass_gener():
    passw_random = ''
    for x in range(6):
        passw_random = ''.join([passw_random,random.choice(list(engl))])

    return passw_random.lower()

def code():
    dom = random.choice('1234567890')
    return dom

def email_gener():
    name_email = ''
    name_server = ''
    for x in range(6):
        name_email = ''.join([name_email,random.choice(engl)])
    for y in range(4):
        name_server = ''.join([name_server,random.choice(engl)])

    def domen():
        dom = random.choice(domens)
        return dom

    email = ''.join([name_email,'@',name_server,'.',domen()])
    return email.lower()

fcv = ''
for x in range(6):
    fcv = fcv + random.choice(list(engl))

login_no_valid = fcv
ls_no_valid = fcv

# if __name__  == '__main__':
#     pass
