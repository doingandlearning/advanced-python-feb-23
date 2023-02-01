from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

print(dir(app))
print(dir(api))

products = [
	{
		"id": 0,
		"description": 'Large slice of pizza',
		"price": 10.00,
		"unitsInStock": 100
	},
	{
		"id": 1,
		"description": 'Brownie',
		"price": 6.00,
		"unitsInStock": 0
	},
	{
		"id": 2,
		"description": 'Can of Coke',
		"price": 3.00,
		"unitsInStock": 1000
	},
	{
		"id": 3,
		"description": 'Straws',
		"price": 0.10,
		"unitsInStock": 10000
	},
	{
		"id": 4,
		"description": 'Garlic Bread',
		"price": 5.50,
		"unitsInStock": 50
	}
]

nextId = 5

class Product(Resource):
	def get(self, id=None):
		if id is None:
			return products, 200
		else:
			for product in products:
				if(id==product["id"]):
					return product, 200
			return "Product not found", 404
	def post(self):
		global nextId
		json_data = request.get_json(force=True)
		product = {
			"id": nextId,
			"description": json_data["description"],
			"price": json_data['price'],
			"unitsInStock": json_data["unitsInStock"]
		}
		products.append(product)
		nextId += 1
		return product, 201
	
	def patch(self, id):
		json_data = request.get_json(force=True)
		for product in products:
			if(id == product["id"]):
				product["description"] = json_data["description"] if json_data["description"] else product["description"]
				product["price"] = json_data["price"] if json_data["price"] else  product["price"]
				product["unitsInStock"] = json_data["unitsInStock"] if json_data["unitsInStock"] else  product["unitsInStock"]
				return product, 200
		return "Product not found", 404

	def delete(self, id):
		for index, product in enumerate(products):
			if(id == product["id"]):
				products.pop(id)
				return "Product deleted", 204
		return "Product not found", 404

api.add_resource(Product, "/api/v1/products", "/api/v1/products/<int:id>")
app.run(debug=True)