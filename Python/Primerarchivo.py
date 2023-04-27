import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["agenda"]

collection = db["contactos"]

documento={"nombre":"Jorge"}
collection.insert_one(documento)

collection.delete_one({"nombre":"Jorge"})
collection.delete_many({"nombre":"Jorge"})

resultados=collection.find({"nombre":"Jorge"})
for resultado in resultados:
        print(resultado)



