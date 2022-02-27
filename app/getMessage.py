from app import app
from app.dataAdapter.mongoAdapter import mongoAdapter
from utils import JSONEncoder

@app.route('/message/<string:id>')
def get_message(id):
    
    db = mongoAdapter(app)
    message = db.get_one(id)
    return JSONEncoder.JSONEncoder().encode(message)

