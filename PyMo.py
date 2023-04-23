import json
import pymongo

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
        pass

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
