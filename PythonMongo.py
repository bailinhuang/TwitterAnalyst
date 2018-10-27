from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://localhost:27017")
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
db = client.test
test = db.test
print(test.find_one())
data = {"name": "Don A"}
data_id = test.insert_one(data).inserted_id
print(test.find_one(data_id))

git filter-branch --force --index-filter
'git rm --cached --ignore-unmatch TwitterConnect.py'
--prune-empty --tag-name-filter cat -- --all