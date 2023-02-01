from pymongo import MongoClient

# Create a MongoClient object and connect to the database
client = MongoClient('mongodb://localhost:27017/')
mydb = client["mydb"]
products = mydb["products"]

# Insert 10 documents
for i in range(10):
    products.insert_one(
        {"name": "Product "+str(i), "price": i*10, "quantity": 20-i})

# Find all documents in the "products" collection and prints them to the console
for product in products.find():
    print(product)

# Updates the price of all products that have a quantity of less than 10 to be 10% more expensive.
products.update_many({"quantity": {"$lt": 10}}, {
                     "$inc": {"price": (0.1*"$price")}})

# Deletes all products that have a price greater than $50.
products.delete_many({"price": {"$gt": 50}})

# Prints the number of products remaining in the collection to the console
print("No of products remaining : ", products.count_documents({}))
