# messaging-app
Message handling application based on python-flask-mongodb-docker. 

# build
> docker-compose up --build

# check web container
> docker exec -it messaging-app-web-1 /bin/bash

---

# api

## hello
> curl -v http://localhost:4001/hello

## get messages
> curl -v http://localhost:4001/messages

## add message
> curl -X 'PUT' http://localhost:4001/message -d '{"sender":"Ryan", "message":"This is a test message."}' -H 'content-type: application/json'

## get single message
> curl -v http://localhost:4001/message/uuid
> curl -v http://localhost:4001/message/621bb0c9ae5dc4000152715a

## delete single message
> curl -X 'DELETE' -v http://localhost:4001/message/uuid
> curl -X 'DELETE' -v http://localhost:4001/message/621bb3a6f9a91c000125835d

---

# tests

> docker exec -it messaging-app_web_1 /bin/bash

> /app# python3 -m unittest tests/app_test.py

