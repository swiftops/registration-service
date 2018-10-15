# Register Microservice

### Introduction
This microservice is core plugin for chatops product. It is used to add custom service,modify and delete existing  microservice as well as filter in mongo service and filter repository.Example:to add custom intent <custom_intent_name>

service api's :

* swiftservice :
	This microservice can be used to add,delete and update master services.
	
* get_master_data :
	This microservice can be used to fetch microservices master data from mongo db.
	
* filterservice :
	This microservice can be used to register,update and delete filter services.
	
* get_filter_service :
	This microservice can be used to fetch filter services data from db.

### Pre-Requisite

1. python 3.6.0 or above version.
2. docker Refer [Install Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04) documentation.	
3. [mongo-db] (https://www.mongodb.com/)
	
## Installation

#### Checkout Repository
```
$git clone https://github.com/swiftops/registration-service.git
```

##### Configuration

Steps :
1. Open system.properties edit database ip and port which is used to establish connection with mongo db. 

### 1. Deploy inside Docker
    
##### Steps to start microservice
Execute the below command to build and run the container
```
docker build -t <image-name>
docker run -p  --name ms-registerservice -d <image-name>
```


### 2. On Commit Auto-deploy on specific server.
---
To autodeploy docker container based service on server used below steps
* You need to configure Gitlab Runner to execute Gitlab CI/CD Pipeline. See [Gitlab Config](https://docs.gitlab.com/runner/install)
As soon as you configure runner auto deployment will start as you commited the code in repository.
refer .gitlab-ci.yml file.


### 3. Deploy on local environment.
----
#### Pre-Requisite
Add pre requisite steps here
#### Create Virtual Environment
Virtualenv is the easiest and recommended way to configure a custom Python environment for your services.
To install virtualenv execute below command:
```sh
$pip3 install virtualenv
```
You can check version for virtual environment version by typing below command:
```sh
$virtualenv --version
```
Create a virtual environment for a project:
```
$ cd my_project_folder
$ virtualenv virtenv
```
virtualenv `virtenv` will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages. The name of the virtual environment (in this case, it was `virtenv`) can be anything; omitting the name will place the files in the current directory instead.

This creates a copy of Python in whichever directory you ran the command in, placing it in a folder named `virtenv`.

You can also use the Python interpreter of your choice (like python3.6).
```
$virtualenv -p /usr/bin/python3.6 virtenv
```
To begin using the virtual environment, it needs to be activated:
```
$ source virtenv/bin/activate
```
The name of the current virtual environment will now appear on the left of the prompt (e.g. (virtenv)Your-Computer:your_project UserName$) to let you know that it’s active. From now on, any package that you install using pip will be placed in the virtenv folder, isolated from the global Python installation. You can add python packages needed in your microservice development within virtualenv. 

#### Install python module dependanceies
```
pip install -r requirements.txt
```
#### To start microservice 
```
python services.py
```
#### To access Microservice Swagger API Documentation
```
http://<yourip>:<port>/ui

Note - To get your IP in api url change host property in swagger.yaml and restart service.