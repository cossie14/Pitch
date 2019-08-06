
import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'sly'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sylviah:sly@localhost/sly'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    
    #  email configurations
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587 
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = 'sylviah.ruto@gmail.com'
    # MAIL_PASSWORD = 'mulu@gift'
    # SUBJECT_PREFIX = 'Pitch'
    # SENDER_EMAIL = 'sylviah.ruto@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sylviah:sly@localhost/sly_test'


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
     '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sylviah:sly@localhost/sly'
    
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}