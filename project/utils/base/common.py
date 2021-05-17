import os

from project import config

config_object = getattr(config, "MainConfig")


def check_admin_auth(request):
    """Проверка ADMIN авторизации по request"""
    admin_token = request.headers.get('ADMIN')
    return admin_token == config_object.ADMIN_SECRET_KEY
