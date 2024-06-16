# sets up and checks the env.py exists
import os
import pymongo
if os.path.exists("env.py"):
    import env

# Constant variables declared in caps
# MONGO_URI pulls data from env.py
# database and collection values are case sensitive
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "ci_Mongo_walkthrough"
COLLECTION = "celebs"

# mongo connection function
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongDB: %s") % e

# conn takes function as value and passes in MONGO_URI as the function argument
conn = mongo_connect(MONGO_URI)

# sets the connected database and collection as the value for the coll variable
coll = conn[DATABASE][COLLECTION]

# This should now be able to connect to the db

# this will delete all data with the first name douglas and return an object that can be unpacked
coll.update_many({"nationality": "american"}, {"$set":{"hair_color": "red, white, blue"}})

documents = coll.find({"nationality": "american"})

# Iterates through the documents obj and unpacks it(prints to make it visible)
for doc in documents:
    print(doc)