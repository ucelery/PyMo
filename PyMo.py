import json
import pymongo

class PyMo:
    def __init__(self, path):
        """
        *params*  
        path: path to credentials.json
        """
        f = open(path)
        data = json.load(f)

        self.credentials = data
        f.close()

        # Check if credentials.json has the keys "user" and "pass"
        self.__validateCredentials();

        # Try to connect to mongoDB
        self.mongoClient = pymongo.MongoClient(f"mongodb+srv://{self.credentials['user']}:{self.credentials['password']}@{self.credentials['clusterAddress']}/?retryWrites=true&w=majority")
        print("Connected to MongoDB!")
        pass

    # Private Methods
    def __validateCredentials(self):
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
