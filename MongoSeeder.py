import pymongo
from pymongo import MongoClient


class MongoSeeder:
    def __init__(self):
        host = 'mongodb'
        client = MongoClient(host=f'{host}')
        self.__db = client.registre

    def bd(self):
        return self.__db

    def seed(self):
        registre = []

        # Valid data
        name = "Durand"
        first_name = "Nathalie"
        ssn = "269054958815780"
        person = {"nom": name, "prenom": first_name, "ssn": ssn}
        registre.append(person)

        self.db.personnes.insert_many(registre)
        cursor = self.db.personnes.find()
        for person in cursor:
            print(person)


print("Filling DB")
MongoSeeder().seed()

client = MongoClient(host="mongodb")
db = client.registre
print("Done")
