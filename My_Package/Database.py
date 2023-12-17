from pymongo import MongoClient

class Database:
    """
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
    """

    def __init__(self):
        """
        Initializes a Database instance.
        """
        self.cluster = None

    def connectToDb(self, username: str, password: str):
        """
        Connects to the MongoDB cluster using the provided username and password.

        Parameters:
            - username (str): MongoDB username.
            - password (str): MongoDB password.
        """
        connectionString = "mongodb+srv://{}:{}@cluster0.pwhfivf.mongodb.net/?retryWrites=true&w=majority".format(username, password)
        try:
            self.cluster = MongoClient(connectionString)
            print("Database connection successful")
        except:
            print("Database connection failed")

    def getCluster(self) -> MongoClient:
        """
        Returns the MongoClient instance representing the connection to the MongoDB cluster.

        Returns:
            - MongoClient: The MongoClient instance.
        """
        return self.cluster

    def createCollection(self, clusterName: str, collectionName: str, schema: dict):
        """
        Creates a new collection in the specified database with the given name and validation schema.

        Parameters:
            - clusterName (str): Name of the database (cluster) where the collection will be created.
            - collectionName (str): Name of the collection to be created.
            - schema (dict): Validation schema for the collection.

        Returns:
            - pymongo.collection.Collection: The newly created collection.
        """
        db = self.cluster[clusterName]
        result = db.create_collection(collectionName, validator=schema)
        return db[collectionName]

    def getCollection(self, clusterName: str, collectionName: str):
        """
        Retrieves an existing collection from the specified database.

        Parameters:
            - clusterName (str): Name of the database (cluster) where the collection exists.
            - collectionName (str): Name of the collection to be retrieved.

        Returns:
            - pymongo.collection.Collection: The requested collection.
        """
        db = self.cluster[clusterName]
        collection = db[collectionName]
        return collection

    def insertDocument(self, collection, document: list):
        """
        Inserts documents into the specified collection.

        Parameters:
            - collection (pymongo.collection.Collection): The collection where documents will be inserted.
            - document (list): List of documents to be inserted.
        """
        result = collection.insert_many(document)

    def getCollectionData(self, collection):
        """
        Retrieves all documents from the specified collection.

        Parameters:
            - collection (pymongo.collection.Collection): The collection from which data will be retrieved.

        Returns:
            - pymongo.cursor.Cursor: Cursor containing the retrieved documents.
        """
        result = collection.find()
        return result

    def updateCollectionData(self, collection, actions: dict):
        """
        Updates password fields for all documents in the specified collection.

        Parameters:
            - collection (pymongo.collection.Collection): The collection to be updated.
            - actions (dict): Dictionary containing actions such as "passwordGenerator" and "sendEmail".
        Notes:
            - This method uses the "passwordGenerator" function to generate new passwords and sends an email to users with their updated passwords using the "sendEmail" function.
        """
        documents = self.getCollectionData(collection)
        for document in documents:
            newPassword = actions["passwordGenerator"](10)
            detail = {"To":document["email"],"Subject":"Password Update","Message":"Your new password is {}".format(newPassword)}
            collection.update_one({"_id": document["_id"]}, {"$set": {"password": newPassword}})
            try:
                actions["sendEmail"](detail)
            except:
                pass

