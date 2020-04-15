import os

basedir=os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY='mykey'
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'sqlilte.data')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('USER_MAIL')    #'sumanthp48@gmail.com'
    MAIL_PASSWORD=os.environ.get('USER_PASSWORD')    #'nabavasuko123'
