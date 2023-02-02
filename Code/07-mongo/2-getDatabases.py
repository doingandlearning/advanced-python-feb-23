from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://dbUser:THISisa1234@cluster0.xrl6f9q.mongodb.net/myFirstDatabase')


# Get a list of all the database names.
dbNames = client.list_database_names()
print(f"Database names: {dbNames}")

# Get the "myFirstDatabase" database, using attribute-style syntax.
db1 = client.myFirstDatabase
print(f"logDb1: {db1}")

# Get the "myFirstDatabase" database, using dictionary-style syntax.
db2 = client['myFirstDatabase']
print(f"logDb2: {db2}")
