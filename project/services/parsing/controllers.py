from flask_restplus import Namespace, Resource
from flask import request, jsonify

from project.decorators import admin_secure
from project.utils.base.parse_metrics import parse_site


api = Namespace('Parse', description='Parsing service')


@api.route('/statistic')
@api.doc(security=["admin_token"])
@api.doc(
    params={
        'domain': {
            'description': 'Domain of site',
            'in': 'query',
            'type': 'string',
            'required': True,
        }
    }
)
class GetStatistic(Resource):
    @admin_secure
    def get(self):
        return jsonify(parse_site(request.params.get("domain")))
