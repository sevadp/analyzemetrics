import os
from functools import wraps
from flask import request

from project import config
from .utils.base.common import check_admin_auth


config_object = getattr(config, "MainConfig")


def admin_secure(f):
    """Админская валидация авторизованности"""

    @wraps(f)
    def wrapped(*args, **kwargs):
        if check_admin_auth(request) is False:
            return dict(message='Authentication Error'), 401
        return f(*args, **kwargs)

    return wrapped
