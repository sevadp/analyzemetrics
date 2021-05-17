import os

from project import config


config_object = getattr(config, "MainConfig")
swagger_authorizations = {
    'bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
    'admin': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'ADMIN-SIGNATURE'
    },
}