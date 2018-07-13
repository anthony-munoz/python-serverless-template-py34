VIRTUALENV_PATH=./.virtualenv/
PYTHON=$(VIRTUALENV_PATH)bin/python
PIP=$(VIRTUALENV_PATH)bin/pip


update-source:
	git reset --hard
	git pull

update-dependencies:
	$(PIP) install -r requirements.txt

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

azure-login:
	az login

azure-configure:
	az webapp deployment user set --user-name {{cookiecutter.azure_username}} --password {{cookiecutter.azure_password}} 
	az group create --name {{cookiecutter.azure_resource_group}} --location "West Europe"
	az appservice plan create --name {{cookiecutter.azure_service_plan}} --resource-group {{cookiecutter.azure_resource_group}} --sku FREE
	az webapp create --resource-group {{cookiecutter.azure_resource_group}} --plan {{cookiecutter.azure_service_plan}} --name {{cookiecutter.azure_app_name}} --runtime "python|{{cookiecutter.python_version}}" --deployment-local-git

azure-remote-repo:

	git remote add azure ${azure_repo} 

init:
	git init 
	git add .
	git commit -m "Initial commit"

deploy:
	git push azure master
 
setup:
	azure-login azure-configure azure-remote-repo init
run:
	deploy
