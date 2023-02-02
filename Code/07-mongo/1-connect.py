from pymongo import MongoClient

# Connect to MongoDB instance on the default host and port.
client1 = MongoClient()

# Or connect to a specific host, port.
client2 = MongoClient('localhost', 27017)

# Or connect via a URL
client3 = MongoClient(
    'mongodb://dbUser:THISisa1234@cluster0.xrl6f9q.mongodb.net/myFirstDatabase')

print("client1: %s " % client1)
print("client2: %s" % client2)
print("client3: %s" % client3)
