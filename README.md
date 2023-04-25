# Setup
First get application credentials from MongoDB and then make a cluster.  

After that make a `credentials.json` file and fill the required fields
```json
# for example
{
    "user": "app_user",
    "password": "sOmeP4ssword",
    "clusterAddress": 
}
```
note: cluster address can be seen in the Mongo URI when connecting your application it should look like this  
```
Mongo URI:
mongodb+srv://app_user:<password>@cluster0.12ggh3p.mongodb.net/?retryWrites=true&w=majority

clusterAddress! "cluster0.12ggh3p.mongodb.net"
```

# Methods
Here are features of PyMo

## PyMo Class

In the following examples, we will make use of the following configuration:

```py
from PyMo import PyMo
pm = PyMo('credentials.json')
```


### init_db

The `init_db` method is used to initialize a database. It takes a single argument, the name of the database.

```py
pm.init_db('Employee')
```

### init_collection

The init_collection method is used to initialize a collection. It takes a single argument, the name of the collection.

```py
pm.init_collection('Employee')
```

### init_db_collection

The `init_db_collection` method is used to initialize a database and a collection. It takes two arguments, the name of the database and the name of the collection.

```py
pm.init_db_collection('Employee', 'information')
```

### CRUD

More information about CRUD can be found at `CRUD Class`. Here's an example of how to use it.

```py
pm = PyMo('credentials.json')
pm.init_db_collection('Employee', 'information')
pm.crud.create_document({'name': 'John', 'age': 25, 'salary': 10000})

```

## CRUD Class

The CRUD Class is used to perform CRUD operations on the database. We will make use of the following configuration to avoid repeating ourselves.

```py
from PyMo import PyMo
pm = PyMo('credentials.json')
pm.init_db_collection('Employee', 'information')
```

### create_document

The `create_document` method is used to create a document. It takes a single argument, the document to be created.

```py
pm.crud.create_document({'name': 'John', 'age': 25, 'salary': 10000})
```

### read_document

The `read_document` method is used to read a document. It takes a single argument, the document to be read.

```py
print(pm.crud.read_document({'name': 'John'}))
```

### update_document

The `update_document` method is used to update a document. It takes two arguments, the document to be updated and the updated document.

```py
pm.crud.update_document({'name': 'John'}, {'name': 'John', 'age': 20})
```

### delete_document

The `delete_document` method is used to delete a document. It takes a single argument, the document to be deleted.

```py
pm.crud.delete_document({'name': 'John'})
```