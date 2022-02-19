from app import app
from app.dataAdapter.mongoAdapter import mongoAdapter
from utils import JSONEncoder

@app.route('/messages')
def get_messages():
    
    db = mongoAdapter(app)
    messages = db.get_all()
    return JSONEncoder.JSONEncoder().encode(list(messages))
