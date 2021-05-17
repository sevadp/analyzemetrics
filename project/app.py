from flask import Flask, Blueprint
from flask_cors import CORS
import os

from project import config
from project.extensions import ExtendedApi
from project.utils.base.const import swagger_authorizations


app = Flask(__name__)
app.config.from_object(getattr(config, "MainConfig"))
app.secret_key = app.config['SECRET_KEY']

api_blueprint = Blueprint('Analyze Metrics API', __name__)

api = ExtendedApi(
    api_blueprint,
    title='Analyze Metrics API documentation',
    version='1.0',
    description='Analyze-Metrics.gameapi spec',
    doc='/docs/',
    authorizations=swagger_authorizations,
)
app.register_blueprint(api_blueprint, url_prefix='/api/v1')

cors = CORS(app, resources={r"/*": {"origins": "*"}})

# from errorhandlers import *
# from project.services.parsing.instance import register_parse
#
# register_parse(api)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
