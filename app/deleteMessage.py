from app import app
from app.dataAdapter.mongoAdapter import mongoAdapter
from utils import JSONEncoder

from flask import abort

@app.route('/message/<string:id>', methods=['DELETE'])
def delete_message(id):

    db = mongoAdapter(app)
    result = db.remove_one(id)

    if result.deleted_count is 1:
        return f'deleted {id}', 202
    else:
        abort(404, f'Message with id {id} not found!')
