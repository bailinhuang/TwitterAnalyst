from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
uri = "mongodb://%s:%s@172.16.202.140:3306" % ("YOUR USERNAME", "YOUR PASSWORD")
client = MongoClient(uri)
db=client.admin
# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)
db = client.test #aqui va la bd, en mi caso se llama test
test = db.test #aqui va la collection, en mi caso tambien se llama test

def insertDB(data):
    global test
    data_id = test.insert_one(data).inserted_id
    print("Se inserta: \n")
    print(test.find_one(data_id))
