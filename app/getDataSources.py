from app import app
from app.dataAdapter.mongoAdapter import mongoAdapter
from utils import JSONEncoder

@app.route('/dataSources')
def get_data_sources():

    db = mongoAdapter(app)
    sources = db.get_all()
    return JSONEncoder.JSONEncoder().encode(list(sources))
