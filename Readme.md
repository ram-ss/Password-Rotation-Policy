# Password Rotation Policy

A Python-based system for managing user data in MongoDB with features like password generation, email notification, and database interaction.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Documentation](#documentation)


## Introduction

This project includes modules for interacting with MongoDB to manage user data. It provides functionalities for generating random passwords and sending email notifications using SMTP.

## Features

List the key features of your project.

- **Database Module (`Database.py`):** Connects to MongoDB, creates collections, inserts documents, and updates password fields.

- **Password Module (`Password.py`):** Generates random passwords with specified characteristics.

- **Notification Module (`Notification.py`):** Sends email notifications using SMTP.

## Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```
# Example code snippet
from My_Package.Database import *
from My_Package.Password import *
from My_Package.Notification import *

# Your code here
```

## Examples

```
# Example usage
from pymongo import MongoClient
from My_Package.Database import Database
from My_Package.Password import Password
from My_Package.Notification import Notification

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
```

## Documentation

- [Database Documentation](#database-documenation)
- [Password Documentation](#password-documentation)
- [Notification Documentation](#notification-documentation)

## Database Documentation

```
Database class for interacting with MongoDB.

    Attributes:
        - cluster: MongoClient instance representing the connection to the MongoDB cluster.

    Methods:
        - __init__():
            Initializes a Database instance.

        - connectToDb(username: str, password: str):
            Connects to the MongoDB cluster using the provided username and password.
            Parameters:
                - username (str): MongoDB username.
                - password (str): MongoDB password.

        - getCluster() -> MongoClient:
            Returns the MongoClient instance representing the connection to the MongoDB cluster.

        - createCollection(clusterName: str, collectionName: str, schema: dict) -> pymongo.collection.Collection:
            Creates a new collection in the specified database with the given name and validation schema.
            Parameters:
                - clusterName (str): Name of the database (cluster) where the collection will be created.
                - collectionName (str): Name of the collection to be created.
                - schema (dict): Validation schema for the collection.
            Returns:
                - pymongo.collection.Collection: The newly created collection.

        - getCollection(clusterName: str, collectionName: str) -> pymongo.collection.Collection:
            Retrieves an existing collection from the specified database.
            Parameters:
                - clusterName (str): Name of the database (cluster) where the collection exists.
                - collectionName (str): Name of the collection to be retrieved.
            Returns:
                - pymongo.collection.Collection: The requested collection.

        - insertDocument(collection: pymongo.collection.Collection, document: list):
            Inserts documents into the specified collection.
            Parameters:
                - collection (pymongo.collection.Collection): The collection where documents will be inserted.
                - document (list): List of documents to be inserted.

        - getCollectionData(collection: pymongo.collection.Collection) -> pymongo.cursor.Cursor:
            Retrieves all documents from the specified collection.
            Parameters:
                - collection (pymongo.collection.Collection): The collection from which data will be retrieved.
            Returns:
                - pymongo.cursor.Cursor: Cursor containing the retrieved documents.

        - updateCollectionData(collection: pymongo.collection.Collection, passwordGenerator: callable):
            Updates password fields for all documents in the specified collection using the provided passwordGenerator function.
            Parameters:
                - collection (pymongo.collection.Collection): The collection to be updated.
                - actions (dict): Dictionary containing actions such as "passwordGenerator" and "sendEmail".
            Notes:
                - This method uses the "passwordGenerator" function to generate new passwords and sends an email to users with their updated passwords using the "sendEmail" function.
```

## Password Documentation

```
Created Password class for generating random passwords with specified characteristics.

    Attributes:
        None

    Methods:
        - generatePassword(length: int) -> str:
            Generates a random password with the specified length and characteristics.
            Parameters:
                - length (int): The desired length of the password.
            Returns:
                - str: The generated password.

        - shufflePassword(arr: str) -> str:
            Shuffles the characters in the provided string to add randomness.
            Parameters:
                - arr (str): The input string to be shuffled.
            Returns:
                - str: The shuffled string.

        - generateRandomNumber() -> str:
            Generates a random numeric character.
            Returns:
                - str: The generated random numeric character.

        - generateLowercase() -> str:
            Generates a random lowercase alphabetical character.
            Returns:
                - str: The generated random lowercase alphabetical character.

        - generateUppercase() -> str:
            Generates a random uppercase alphabetical character.
            Returns:
                - str: The generated random uppercase alphabetical character.

        - generateSymbol() -> str:
            Generates a random symbol from a predefined set.
            Returns:
                - str: The generated random symbol.
```

## Notification Documentation

```
Notification class for sending emails using SMTP.

    Attributes:
        - __username (str): The username used for authentication.
        - __password (str): The password used for authentication.

    Methods:
        - __init__(username: str, password: str):
            Initializes a Notification instance.

        - getUsername() -> str:
            Returns the username used for authentication.

        - getPassword() -> str:
            Returns the password used for authentication.

        - composeMessage(details: dict) -> str:
            Composes an email message based on the provided details.
            Parameters:
                - details (dict): A dictionary containing email details, including "To", "Subject", and "Message".
            Returns:
                - str: The composed email message as a string.

        - sendEmail(recipient: list):
            Sends emails to the specified recipients based on the provided details.
            Parameters:
                - recipient (list): A list of dictionaries, each containing details for a recipient, including "To", "Subject", and "Message".
```