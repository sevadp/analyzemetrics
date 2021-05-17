import os

from project import config


config_object = getattr(config, os.environ['APP_SETTINGS'])
swagger_authorizations = {
    'admin_token': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'ADMIN'
    }
}
