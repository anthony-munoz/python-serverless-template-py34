# coding: utf-8

import logging
import json
import time
import datetime


from flask_restplus import Resource
from app.rest.api import api
from app.rest.{{cookiecutter.app_name}}.serializers import {{cookiecutter.app_name}}_serializer
from app.{{cookiecutter.app_name}}.{{cookiecutter.app_name}} import {{cookiecutter.app_name}}Controller

log = logging.getLogger(__name__)
ns = api.namespace('{{cookiecutter.app_name}}', description='Information for the dummy service')


@ns.route('/dummy_service')
class {{cookiecutter.app_name}}(Resource):

    @api.expect({{cookiecutter.app_name}}_serializer, validate=True)
    def get(self):
        instance = {{cookiecutter.app_name}}Controller()
        return instance.controller(**api.payload)
        
    @api.expect({{cookiecutter.app_name}}_serializer, validate=True)
    def post(self):
        instance = {{cookiecutter.app_name}}Controller()
        return instance.controller(**api.payload)
    

