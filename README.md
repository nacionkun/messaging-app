# messaging-app
Message handling application based on python-flask-mongodb-docker. 

# build
docker-compose up --build

# check web container
docker exec -it messaging-app-web-1 /bin/bash

# api

## hello
curl -v http://localhost:4001/hello

## get data sources
curl -v http://localhost:4001/dataSources