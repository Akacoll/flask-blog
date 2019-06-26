import os
class Obj:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

o = Obj()

print(o.MAIL_USERNAME)
print(o.MAIL_PASSWORD)
print(o.SQLALCHEMY_DATABASE_URI)
print(o.SECRET_KEY)