import logging
import os
import json
import base64


from app.flask_factory import settings
log = logging.getLogger(__name__)


class {{cookiecutter.app_name}}Controller:

	def __init__(self):
		self.type = "{{cookiecutter.app_name}}"

	def controller(self, user):
		response = 'User information for {{cookiecutter.app_name}}'

		return response
