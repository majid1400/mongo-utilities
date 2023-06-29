from mongo.database import MongoStorage

if __name__ == "__main__":
    a = MongoStorage('testCollection')
    a.store({'key': 'value'})
    # data = a.load({'key kamal2222': 'ww'})
    # a.update({'_id': data.get('_id')}, {'key kamal2222': 'ffff'})
    # a.delete({'key kamal2222': 'ffff'})
