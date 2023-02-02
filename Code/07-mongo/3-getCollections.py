from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://dbUser:THISisa1234@cluster0.xrl6f9q.mongodb.net/myFirstDatabase')

db = client.test

# Get the "log" collection, using attribute-style syntax.
log1 = db.log
print(f"log1: {log1}")

# Get the "log" collection, using dictionary-style syntax.
log2 = db['log']
print(f"log2: {log2}")
