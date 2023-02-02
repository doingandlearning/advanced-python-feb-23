from flask import Flask, request
from requests import get

app = Flask(__name__)

# Building a CRUD API from scratch

# Proxying an API
@app.before_request
def auth_function():
	if(not request.headers.get("x-api-key")):
		return ({"error": True, "message": "Requires x-api-key"}, 403)
	if (request.headers.get("x-api-key") != "flaskisawesome"):
		return ({"error": True, "message": "Incorrect x-api-key"}, 403)

@app.route("/", methods=["POST"])
def hello_world():
	return "<p>Hello World!</p>"


todos = {}
nextId = 1

# GET    /api/todos
@app.route("/api/todos", methods=["GET"])
def getAllTodos():
	return list(todos.values())


# POST   /api/todos
@app.route("/api/todos", methods=["POST"])
def createTodo():
	global nextId
	todo = request.get_json()
	todo["id"] = nextId
	todos[nextId] = todo
	nextId += 1
	return todo


# GET    /api/todos/id
@app.route("/api/todos/<int:id>", methods=["GET"])
def getTodoById(id):
	if id not in todos.keys():
		return ({"error": True, "message": "Todo doesn't exist"}, 404)
	return todos[id]


# PATCH  /api/todos/id
@app.route("/api/todos/<int:id>", methods=["PATCH"])
def updateTodoById(id):
	todos[id] = todos[id] | request.get_json()
	return todos[id]

# DELETE /api/todos/id
@app.route("/api/todos/<int:id>", methods=["DELETE"])
def deleteTodoById(id):
	if id not in todos.keys():
		return ({"error": True, "message": "Todo doesn't exist"}, 404)
	del todos[id]
	return ({}, 204)


# https://api.openweathermap.org/data/2.5/weather?q=London&appid=0de6bc7ec1efaff74b56d2bab3b38f6e&units=metric

API_KEY = "0de6bc7ec1efaff74b56d2bab3b38f6e"

@app.route("/api/weather/<city>", methods=["GET"])
def getWeatherByCity(city):
	# get the city from the request
	# query the weather api 
	response = get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric").json()
	# parse the weather api and send back other information
	del response['coord']
	response["best_city"] = True
	# send the response
	return response