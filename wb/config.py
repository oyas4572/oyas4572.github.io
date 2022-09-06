import os

class Config:
    #Database

    SECRET_KEY = '123'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    #mail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "tt2413682@gmail.com"
    MAIL_PASSWORD = "nwobnprvctxwnqub"

    # app.config['MAIL_USE_TLS'] = False
    # app.config['MAIL_USE_SSL'] = True