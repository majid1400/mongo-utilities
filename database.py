from typing import Union

from mongo.client import MongoDatabase


class MongoStorage:
    def __init__(self, collection):
        self.mongo = MongoDatabase()
        self.collection = collection

    def store(self, data: Union[dict, list]):
        collection = getattr(self.mongo.database, self.collection)
        try:
            if isinstance(data, list) and len(data) > 1:
                collection.insert_many(data)
            else:
                collection.insert_one(data)
        except Exception as e:
            return {"Error": e}

    def load(self, query: dict = None):
        try:
            return self.mongo.database[self.collection].find(query)[0]
        except Exception as e:
            return {"Error": e}

    def delete(self, query: Union[dict, list]):
        collection = getattr(self.mongo.database, self.collection)
        try:
            if isinstance(query, list) and len(query) > 1:
                collection.delete_many(query)
            else:
                collection.delete_one(query)
        except Exception as e:
            return {"Error": e}

    def update(self, old_value: dict, new_value: dict):
        collection = getattr(self.mongo.database, self.collection)
        try:
            collection.update_one(old_value, {"$set": new_value})
        except Exception as e:
            return {"Error": e}
