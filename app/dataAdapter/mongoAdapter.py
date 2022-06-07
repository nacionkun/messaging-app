from bson.objectid import ObjectId
from flask_pymongo import PyMongo

import os

mongo = None

class mongoAdapter:

    # constructor
    def __init__(self, app):
        self.app = app

    def __get_mongo(self):
        global mongo

        # MONGO=mongodb://mongo/r1v4 --> check docker-compose.yaml
        # app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
        # getenv: if MONGO env param not found, use explicit default param
        # HOST 2001/TCP is mapped to CONTAINER 27107/TCP
        if 'MONGO_URI' not in self.app.config:
            self.app.config['MONGO_URI'] = os.getenv(
                'MONGO', 'mongodb://localhost:2001/mdb_r1v4') 

        if not mongo:
            mongo = PyMongo(self.app)

        return mongo

    def get_all(self):
        return self.__get_mongo().db.messages.find({})

    def add_one(self, data):
        return self.__get_mongo().db.messages.insert_one(data)

    def remove_one(self, id):
        return self.__get_mongo().db.messages.delete_one({'_id': ObjectId(id)})

    def get_one(self, id):
        return self.__get_mongo().db.messages.find_one_or_404(ObjectId(id))

