


import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

with open(os.path.join("settings", "mongodb_uri.txt")) as f:
    uri = f.read()

if uri == "<uri_here>":
    raise Exception("Please insert URI for Mongo database in ./settings/mongodb_uri.txt")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

mongodb = client["usersystembackend"]
