from pymongo import *
from My_Package.Database import *
from My_Package.Password import *
from My_Package.Notification import *

# JSON schema for the MongoDB collection
schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["email", "password"],
        "properties": {
            "email": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "password": {
                "bsonType": "string",
                "description": "must be a string and is required"
            }
        }
    }
}

# Sample user data
data = [
    {"email": "abc@gmail.com", "password": "123"},
    {"email": "pqr@gmail.com", "password": "456"},
    {"email": "xyz@gmail.com", "password": "789"},
]

# Create instances of the Database, Password, and Notification classes
instance = Database()
pas = Password()
notification = Notification(username="", password="")

# Connect to the MongoDB cluster
instance.connectToDb(username="", password="")

# Create a collection named "User" with the defined schema
instance.createCollection(clusterName="Cluster0", collectionName="User", schema=schema)

# Insert sample user data into the "User" collection
collection = instance.getCollection(clusterName="Cluster0", collectionName="User")
instance.insertDocument(collection=collection, document=data)

# Update passwords in the "User" collection using the Password class and send email notifications
collection = instance.getCollection(clusterName="Cluster0", collectionName="User")
instance.updateCollectionData(collection=collection, actions={"passwordGenerator": pas.generatePassword, "sendEmail": notification.sendEmail})
