from pymongo import MongoClient

client = MongoClient() 
db = client.test
people = db.people

people.insert_one(
    { "name": "Jayne",  "age": 52, "gender": "F" }
)

people.insert_many([
    { "name": "Thomas", "age": 20, "gender": "M" },
    { "name": "Emily",  "age": 20, "gender": "F", "favTeam": "Swans" }
])
