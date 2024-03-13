from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://USER:PASSWORD@CLUSTER.ha5rmqa.mongodb.net/?retryWrites=true&w=majority&appName=zeosserkluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), )

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Choose your database and collection
db = client['joe']
collection = db['stuff']

# Create a document to add
document = {"name": "John Doe", "age": 30, "city": "New York"}

# Add the document to the collection
insert_result = collection.insert_one(document)

# Print the ID of the inserted document
print(f"Inserted document with ID: {insert_result.inserted_id}")
