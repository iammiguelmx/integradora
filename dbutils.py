from pymongo import MongoClient

MONGO_URI = 'mongodb+srv://miguel:porpuse2019@cluster0-o9vce.mongodb.net/test?retryWrites=true&w=majority'

def db_connect(MONGO_URI, db_name, col_name):
    client = MongoClient(MONGO_URI)
    database = client[db_name]
    collection = database[col_name]
    return collection

def db_insert_user(collection, user):
    return collection.insert_one(user)

def db_insert_vol(collection, voluntariado):
    return collection.insert_one(voluntariado)

def db_insert_reporte(collection, reporte):
    return collection.insert_one(reporte)

def db_find_all(collection, query={}):
    return collection.find(query)

def db_find_one(collection, query={}):
    return collection.find_one(query)

if __name__ == '__main__':
    print("MongoClient imported successfully!")