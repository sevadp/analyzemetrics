import os
import datetime


class MainConfig(object):
    """Production configuration."""
    APP_SETTINGS = "MainConfig"
    ADMIN_SECRET_KEY = "not_real_secret_key"
    SECRET_KEY = "Sofb23foubSHmscb340vm"

    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    STRIPE_SECRET_KEY = 'foo'
    STRIPE_PUBLISHABLE_KEY = 'bar'
    PERMANENT = True
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=365)

    metrics_url = "https://spymetrics.ru/ru/website/"
