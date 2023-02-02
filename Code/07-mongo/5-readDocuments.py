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

allPersons = people.find()
printItems("All persons", allPersons)
person1 = people.find_one({"name": "Kevin"})
pprint.pprint(person1)

somePersons = people.find({
    "name":   {"$regex": "^J"},
    "gender": "F",
    "$or": [
        {"age": {"$lte": 20}},
        {"age": {"$gt": 30}}
    ]
})
printItems("Some persons", somePersons)
