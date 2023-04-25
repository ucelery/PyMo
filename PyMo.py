import json
import pymongo

class PyMo_CRUD:
    def __init__(self, collection = None):
        self.collection = collection
        
    def set_collection(self, collection):
        self.collection = collection
    
    def create_document(self, document):
        """
        Description: Adds a document to the collection\n
        `document: dict` - document to be added
        """
        self.collection.insert_one(document)
        
    def read_document(self, document):
        """
        Description: Reads a document from the collection\n
        `document: dict` - document to be read
        """
        return self.collection.find_one(document)
        
    def delete_document(self, document):
        """
        Description: Removes a document from the collection\n
        `document: dict` - document to be removed
        """
        self.collection.delete_one(document)

    def update_document(self, document, new_document):
        """
        Description: Updates a document in the collection\n
        `document: dict` - document to be updated\n
        `new_document: dict` - new document
        """
        self.collection.replace_one(document, new_document)

class PyMo:
    def __init__(self, path):
        """
        Description: Sets up mongoDB\n
        `path: string` - path to your credentials.json
        """
        f = open(path)
        data = json.load(f)

        self.credentials = data
        f.close()

        # Check if credentials.json has the keys "user" and "pass"
        self.__validate_credentials();

        # Try to connect to mongoDB
        self.mongoClient = pymongo.MongoClient(f"mongodb+srv://{self.credentials['user']}:{self.credentials['password']}@{self.credentials['clusterAddress']}/?retryWrites=true&w=majority")

        self.crud = PyMo_CRUD()

    def init_db(self, db_name):
        """
        Description: Initializes a database\n
        `db_name: string` - name of the database
        """
        self.db = self.mongoClient[db_name]

    def init_collection(self, collection_name):
        """
        Description: Initializes a collection\n
        `collection_name: string` - name of the collection
        """
        self.collection = self.db[collection_name]
        self.crud = PyMo_CRUD(self.collection)

    def init_db_collection(self, db_name, collection_name):
        """
        Description: Initializes a database and collection\n
        `db_name: string` - name of the database\n
        `collection_name: string` - name of the collection
        """
        self.init_db(db_name)
        self.init_collection(collection_name)

    # Private Methods
    def __validate_credentials(self):
        """
        Description: Validates user mongoDB credentials by checking if JSON has the required keys (user, password, clusterAddress)
        """
        keys_list = []
        if not 'user' in self.credentials:
            keys_list.append("user")
        if not 'password' in self.credentials:
            keys_list.append("password")
        if not 'clusterAddress'in self.credentials:
            keys_list.append("clusterAddress")

        keys_str = ", ".join(keys_list)

        if len(keys_list) != 0:
            raise Exception(f"Invalid credentials missing key/s: {keys_str}")
