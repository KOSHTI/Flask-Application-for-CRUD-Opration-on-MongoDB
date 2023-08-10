from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import json

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['users']

# to convert objectId into json format
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)

# Get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = list(collection.find({}))
    # to convert data in json format (thik hai......!!)
    return JSONEncoder().encode(users)

# Get single user by id
@app.route('/users/<string:user_id>', methods=['GET'])           # userid is in a string format
def get_user(user_id):
    user = collection.find_one({'_id': ObjectId(user_id)}, {'_id': 0})
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = collection.insert_one(data).inserted_id
    return jsonify({'message': 'User created successfully', 'user_id': str(user_id)})

# Update user by id
@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    result = collection.update_one({'_id': ObjectId(user_id)}, {'$set': data})
    if result.modified_count == 1:
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404

# Delete user by id
@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = collection.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404
    
if __name__ == '__main__':
    app.run(debug=True)