from pymongo import MongoClient
from pandas import DataFrame as df

def get_database():
    CONNECTION_STRING = "mongodb://root:6wTYD4gi78yIgTPx@ac-vhitqap-shard-00-00.rj2pktu.mongodb.net:27017,ac-vhitqap-shard-00-01.rj2pktu.mongodb.net:27017,ac-vhitqap-shard-00-02.rj2pktu.mongodb.net:27017/?ssl=true&replicaSet=atlas-14026p-shard-0&authSource=admin&retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    dbname = client['dogs']  # dogs database
    records = dbname["records"]  #hier creer je een nieuwe collection of open je een bestaande
    return records

def insertData(id, data, collection):

    dog = []
    start = ""
    end = ""
    ftype = ""
    message = ""
    count = 0
    for dicts in data:
        if count < 4:
            dog.append(dicts)
            count +=1
        else:
            for key, value in dicts.items():
                if key == "startTime":
                    start = value
                if key == "endTime":
                    end = value
                if key == "formType":
                    ftype = value
                if key == "exception":
                    message = value

    id_index = collection.create_index("_id")
    item_1 = {"_id": id, "dogs": dog, "StartTime": start, "Endtime": end, "FormType": ftype, "Message": message}
    collection.insert_one(item_1)

def getData(id,collection):

    item_details = collection.find({"_id": id})
    panda = df(item_details)
    item = 0
    for row, data in panda.iterrows():
        item = data["dogs"]

    return item

def addResearch(id, data, collection):

    final = ""
    V1 = ""
    V2 = ""
    V3 = ""
    V4 = ""
    for dicts in data:
        for key, value in dicts.items():
            if key == "finalTime":
                final = value
            if key == "V1":
                V1 = value
            if key == "V2":
                V2 = value
            if key == "V3":
                V3 = value
            if key == "V4":
                V4 = value

    new_value1 = {"$set": {"V1": V1}}
    new_value2 = {"$set": {"V2": V2}}
    new_value3 = {"$set": {"V3": V3}}
    new_value4 = {"$set": {"V4": V4}}
    new_value5 = {"$set": {"FinalTime": final}}


    filtered = {"_id": id}

    collection.update_one(filtered, new_value1)
    collection.update_one(filtered, new_value2)
    collection.update_one(filtered, new_value3)
    collection.update_one(filtered, new_value4)
    collection.update_one(filtered, new_value5)

    return "succesfully exported research"

def exitdb():
    CONNECTION_STRING = "mongodb://root:6wTYD4gi78yIgTPx@ac-vhitqap-shard-00-00.rj2pktu.mongodb.net:27017,ac-vhitqap-shard-00-01.rj2pktu.mongodb.net:27017,ac-vhitqap-shard-00-02.rj2pktu.mongodb.net:27017/?ssl=true&replicaSet=atlas-14026p-shard-0&authSource=admin&retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    client.close()

