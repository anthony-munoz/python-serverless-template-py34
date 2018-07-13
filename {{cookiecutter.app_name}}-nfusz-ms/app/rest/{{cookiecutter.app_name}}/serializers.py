import json
from flask_restplus import fields
from app.router import api


context_example = {
        "title": 'Welcome',
        "content": 'We are pleased to have you on board!',
        "action_content": 'More information in our web application.',
        "action_title": 'nFusz',
        "action_url": 'https://nfusz.com',
        "action_text": 'Your CRM platform',
    }


{{cookiecutter.app_name}}_serializer = api.model('Resource', {
    'variable': fields.String(required=True, description='dummy description', example="Hi world"),
})
