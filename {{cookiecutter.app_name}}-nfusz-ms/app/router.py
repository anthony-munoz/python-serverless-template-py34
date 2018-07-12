import traceback
import logging
from app.flask_factory import settings
from flask import Blueprint
from flask_cors import CORS
from app.rest.api import api
from app.rest.{{cookiecutter.app_name}}.api import ns as {{cookiecutter.app_name}}_namespace


log = logging.getLogger(__name__)


def _configure_namespaces(api):
	"""
		Add more namespaces HERE
	"""
	#{{cookiecutter.app_name}}_namespace
	api.add_namespace({{cookiecutter.app_name}}_namespace)


def configure_api(flask_app):
	blueprint = Blueprint('api', __name__)
	api.init_app(blueprint)
	_configure_namespaces(api)
	CORS(flask_app)
	flask_app.register_blueprint(blueprint)
