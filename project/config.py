import os
import datetime


class MainConfig(object):
    """Production configuration."""
    APP_SETTINGS = os.environ['APP_SETTINGS']
    ADMIN_SECRET_KEY = os.environ['ADMIN_SECRET_KEY']
    SECRET_KEY = os.environ['SECRET_KEY']
    SERVER_NAME = os.environ['SERVER_NAME']

    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    STRIPE_SECRET_KEY = 'foo'
    STRIPE_PUBLISHABLE_KEY = 'bar'
    PERMANENT = True
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=365)
