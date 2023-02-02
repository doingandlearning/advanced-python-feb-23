from pymongo import MongoClient
import pprint

def printItems(message, items):
    print(message)
    for i in items:
        pprint.pprint(i)
  
  
# main code
client = MongoClient() 
db = client.test
people = db.people

people.delete_one(
    { "name": "Wilfried" }
)

people.delete_many(
    { "favouriteTeam": "Cardiff" }
)

people.delete_many(
    { "overdraft": { "$exists": True } }
)

printItems("People", people.find())   