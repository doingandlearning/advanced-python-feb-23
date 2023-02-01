from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Greet(Resource):
    def get(self, name):
        return {'greet': name}

    def post(self):
        data = request.get_json()
        name = data['name']
        return {'greet': name}


users = {}
nextId = 1


class UserList(Resource):
    def get(self):
        global users
        return users

    def post(self):
        global users
        global nextId
        users[nextId] = request.get_json()
        nextId += 1
        return users

    def patch(self, id):
        global users
        if id not in users.keys():
            return ({"error": True, "message": "User not found"}, 404)
        users[id] = users[id] | request.get_json()
        return users[id]

    def delete(self, id):
        global users
        if id not in users.keys():
            return ({"error": True, "message": "User not found"}, 404)
        del users[id]
        return ({}, 201)


api.add_resource(HelloWorld, '/')
api.add_resource(Greet, '/greet/string:name')
api.add_resource(UserList, '/users', '/users/<int:id>')

if __name__ == '__main__':
    app.run()
