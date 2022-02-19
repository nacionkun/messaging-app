# messaging-app
Message handling application based on python-flask-mongodb-docker. 

# build
docker-compose up --build

# check web container
docker exec -it messaging-app-web-1 /bin/bash

# api

## hello
curl -v http://localhost:4001/hello

## get messages
curl -v http://localhost:4001/messages

## add message
curl -X 'PUT' http://localhost:4001/message -d '{"sender":"Ryan", "message":"This is a test message."}' -H 'content-type: application/json'
