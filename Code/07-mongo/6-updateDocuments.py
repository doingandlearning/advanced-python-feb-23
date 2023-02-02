from pymongo import MongoClient
import pprint


def printItems(message, items):
    print(message)
    for i in items:
        pprint.pprint(i)


# main code
client = MongoClient(
    'mongodb+srv://dbUser:THISisa1234@cluster0.xrl6f9q.mongodb.net/myFirstDatabase')
db = client.myFirstDatabase
people = db.log

people.update_one(
    {"name": "Jane"},
    {"$set": {"name": "JAYNE", "favTeam": "Swans"}}
)

people.update_many(
    {},
    {"$inc": {"age": 1}}
)

people.update_many(
    {},
    {"$rename": {"favTeam": "favouriteTeam"}}
)

printItems("People", people.find())
