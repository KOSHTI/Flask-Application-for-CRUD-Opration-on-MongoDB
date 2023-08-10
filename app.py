from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import json
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['users']

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)

class User(Resource):
    def get(self, user_id=None):
        if user_id:
            user = collection.find_one({'_id': ObjectId(user_id)}, {'_id': 0})
            if user:
                return jsonify(user)
            else:
                return {'message': 'User not found'}, 404
        else:
            users = list(collection.find({}))
            return JSONEncoder().encode(users)
    
    def post(self):
        data = request.get_json()
        user_id = collection.insert_one(data).inserted_id
        return {'message': 'User created successfully', 'user_id': str(user_id)}
    
    def put(self, user_id):
        data = request.get_json()
        result = collection.update_one({'_id': ObjectId(user_id)}, {'$set': data})
        if result.modified_count == 1:
            return {'message': 'User updated successfully'}
        else:
            return {'message': 'User not found'}, 404
    
    def delete(self, user_id):
        result = collection.delete_one({'_id': ObjectId(user_id)})
        if result.deleted_count == 1:
            return {'message': 'User deleted successfully'}
        else:
            return {'message': 'User not found'}, 404

# Add the User resource to the API with specific routes
api.add_resource(User, '/users', '/users/', '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
