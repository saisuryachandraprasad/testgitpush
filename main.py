import pymongo

client = pymongo.MongoClient("mongodb+srv://saisuryachandraprasad:saichandrass@cluster0.kqzmmk8.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d ={
    'name':"saichandraprasad",
    'email':'saisuryachandraprasad@gmail.com',
    'mobile': 9618421637
}

db1 =client['mongodbtest']
coll = db1['test']
coll.insert_one(d)