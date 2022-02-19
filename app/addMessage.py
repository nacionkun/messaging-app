from app import app
from app.dataAdapter.mongoAdapter import mongoAdapter

from flask import abort, request
from utils import JSONEncoder
from bson.objectid import ObjectId

@app.route('/message', methods=['PUT'])
def add_message():

    # Remove force=True when releasing code!
    json_data = request.get_json(force=True, silent=True, cache=False)

    if not json_data or 'sender' not in json_data or 'message' not in json_data:
        abort(400, f'provided json payload is incorrect!')

    messageSet = {
        'sender': json_data["sender"],
        'message': json_data["message"]
    }

    _id = json_data.get('_id', None)

    if _id is not None:
        messageSet['_id'] = ObjectId(_id)

    db = mongoAdapter(app)
    result = db.add_one(messageSet)

    return JSONEncoder.JSONEncoder().encode(result.inserted_id), 201
