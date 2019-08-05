
import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'sly'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sylviah:sly@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch'
    SENDER_EMAIL = 'sylviah.ruto@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vincent:Empharse333@localhost/pitch_test'


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
    
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