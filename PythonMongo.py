from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
uri = "mongodb://%s:%s@172.16.202.140:3306" % ("bailin", "6WcDhJG3YCy5NVom")
#uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db=client.admin
# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)
db = client.db_proyecto #aqui va la bd, en mi caso se llama test
tweets = db.tweets_bendecir_es  #aqui va la collection, en mi caso tambien se llama test

def insertDB(data):
    global tweets
    data_id = tweets.insert_one(data).inserted_id
    print("Se inserta: \n")
    print(tweets.find_one(data_id))
