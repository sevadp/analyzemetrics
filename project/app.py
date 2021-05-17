from flask_cors import CORS
from flask import Flask, Blueprint
import os

from project import config
from project.extensions import ExtendedApi
from project.utils.base.const import swagger_authorizations


app = Flask(__name__, subdomain_matching=True)
app.config.from_object(getattr(config, "MainConfig"))
app.secret_key = app.config['SECRET_KEY']

api_blueprint = Blueprint('Adopt goods API', __name__)
api = ExtendedApi(
    api_blueprint,
    title='Adopt goods API documentation',
    version='1.0',
    description='adopt-goods spec',
    doc='/docs/',
    authorizations=swagger_authorizations,
)
app.register_blueprint(api_blueprint, url_prefix='/api/v1')

cors = CORS(app, resources={r"/*": {"origins": "*"}})


if __name__ == '__main__':
    app.run()
