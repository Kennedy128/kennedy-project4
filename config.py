import os
class Config:
  '''
  General configuration parent class
  '''
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kennedy:Kennedy128@localhost/blogers'
  UPLOADED_PHOTOS_DEST='app/static/photos'
  #  email configurations
  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  #simple mde configurations
  SIMPLEMDE_JS_IIFE=True
  SIMPLEMDE_USE_CDN=True
class ProdConfig(Config):
  '''
  Production configuration child class
  Args:
    Config: The parent configuration class with general configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kennedy:Kennedy128@localhost/blogers_test'

class DevConfig(Config):
  '''
  Development configuration child class
  Args:
    Config: The parent configuration class with General configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kennedy:Kennedy128@localhost/blogers'
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}