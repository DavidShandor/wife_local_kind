from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import logging
import os
from bson import ObjectId
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, make_wsgi_app, Gauge, Histogram

app = Flask(__name__)
# hello world!
# connect to Prometheus Metrics
metrics = PrometheusMetrics(app)

request_counter = Counter('requests_total', 'Total number of requests')
contacts_count_gauge = Gauge('contacts_total', 'Total number of contacts in the database')
request_latency_histogram = Histogram('request_latency_seconds', 'Request latency in seconds', buckets=(0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, float("inf")))

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get environment variables
MONGO_URI = os.environ.get('MONGO_URI','mongodb://mongodb:27017/wife_todo_list')
DB_NAME = os.environ.get('DB_NAME', 'wife_todo_list')

if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
missions = db['missions']

@app.route('/')
def index():
    mission_list = list(missions.find())
    for mission in mission_list:
        mission['_id'] = str(mission['_id'])
    return render_template('index.html', missions=mission_list)

@app.route('/mission', methods=['GET'])
def get_missions():
    mission_ids = [str(mission['_id']) for mission in missions.find()]
    logger.info(f"Retrieved {len(mission_ids)} mission IDs")
    return jsonify(mission_ids)

@app.route('/mission', methods=['POST'])
def create_mission():
    data = request.form.to_dict()
    result = missions.insert_one(data)
    logger.info(f"Created new mission: {result.inserted_id}")
    return jsonify({"message": "Mission created", "id": str(result.inserted_id)}), 201

@app.route('/mission/<string:id>', methods=['GET'])
def get_mission(id):
    mission = missions.find_one({'_id': ObjectId(id)})
    if mission:
        mission['_id'] = str(mission['_id'])
        logger.info(f"Retrieved mission: {id}")
        return jsonify(mission)
    logger.warning(f"Mission not found: {id}")
    return jsonify({"error": "Mission not found"}), 404

@app.route('/mission/<string:id>', methods=['PUT'])
def update_mission(id):
    data = request.json
    result = missions.update_one({'_id': ObjectId(id)}, {'$set': data})
    if result.modified_count:
        logger.info(f"Updated mission: {id}")
        return jsonify({"message": "Mission updated"})
    logger.warning(f"Mission not found for update: {id}")
    return jsonify({"error": "Mission not found"}), 404

@app.route('/mission/<string:id>', methods=['DELETE'])
def delete_mission(id):
    result = missions.delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        logger.info(f"Deleted mission: {id}")
        return jsonify({"message": "Mission deleted"})
    logger.warning(f"Mission not found for deletion: {id}")
    return jsonify({"error": "Mission not found"}), 404

@app.route('/metrics')
def metrics():
    return make_wsgi_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)