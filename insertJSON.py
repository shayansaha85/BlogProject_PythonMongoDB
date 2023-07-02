from pymongo import MongoClient


def insertBlog(data):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['admin']
    collection = db['TEST'] 
    collection.insert_one(data)
    print("Document inserted with ID:", data["_id"])