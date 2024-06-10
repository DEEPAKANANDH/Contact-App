import pymongo


dbConnect = pymongo.MongoClient("mongodb://localhost:27017")

database = dbConnect["Library"]

dbCollection = database["Books"]
