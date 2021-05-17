from .controllers import api


def register_parse(app):
    app.add_namespace(api, path='/parse')
