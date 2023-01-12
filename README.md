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