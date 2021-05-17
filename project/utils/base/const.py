import os

from project import config


config_object = getattr(config, "MainConfig")
swagger_authorizations = {
    'admin_token': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'ADMIN'
    }
}
