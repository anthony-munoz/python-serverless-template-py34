# coding: utf-8

import logging
import json
import time
import datetime


from flask_restplus import Resource
from app.rest.api import api
from app.rest.{{cookiecutter.app_name}}.serializers import stats_serializer
from app.{{cookiecutter.app_name}}.{{cookiecutter.app_name}} import {{cookiecutter.app_name}}Controller

log = logging.getLogger(__name__)
ns = api.namespace('{{cookiecutter.app_name}}', description='Get statistics users information in your notifiCRM account')


@ns.route('/get_user_information')
class Stats(Resource):

    @api.expect(stats_serializer, validate=True)
    def get(self):
        post_mail = {{cookiecutter.app_name}}Controller()
        return post_mail.controller(**api.payload)

