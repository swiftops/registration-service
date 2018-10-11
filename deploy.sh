#!/bin/bash
export HOST_IP=<HOST_IP>
cd <path>  					#service repository path  
docker-compose scale <service_name>=0 	#scale services to 0.
docker rmi -f <service_image> && docker pull <service_image> && docker-compose up -d --remove-orphans
