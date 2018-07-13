
{{cookiecutter.app_name}} Azure MicroService based on Serverless 

Describe your App Here

Getting Started

cookiecutter <git url project>

- Install azure cli on your local enviroment to make easy initial setup
- After install cli azure, run command

az login

- then sign in with your credentials account in window browser that automatically open after run before command
- you should see something like a json config with your status microsoft account
- Next steps are when you can deploy your application
- Create a deployment user

az webapp deployment user set --user-name <username> --password <password> 

Example 

az webapp deployment user set --user-name toni5705_test --password toni5705_testM 

- Create a resource group


az group create --name toniResourceGroup --location "West Europe"

- Create an Azure App Service plan

az appservice plan create --name toniAppServicePlan --resource-group toniResourceGroup --sku FREE

- Create a web app

az webapp create --resource-group toniResourceGroup --plan toniAppServicePlan --name toniApp --runtime "python|3.4" --deployment-local-git

- Create a git remote app

git init 


git remote add azure <git url given that before step> 


git add .


git commit -m "Initial commit"


- Push to Azure git with auto deploy your app

git push azure master

# Python Flask app on Azure App Service Web

This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service Web.

This repository can directly be deployed to Azure App Service.

For more information, please see the [Python on App Service Quickstart docs](https://docs.microsoft.com/en-us/azure/app-service-web/app-service-web-get-started-python).

# Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
