azure-login:
	az login

azure-configure:
	az webapp deployment user set --user-name {{azure_username}} --password {{azure_password}} 
	az group create --name {{azure_resource_group}} --location {{azure_resource_location}}
	az appservice plan create --name {{azure_service_plan}} --resource-group {{azure_resource_group}} --sku FREE
	az webapp create --resource-group {{azure_resource_group}} --plan {{azure_service_plan}} --name {{azure_app_name}} --runtime "python|{{python_version}}" --deployment-local-git

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
