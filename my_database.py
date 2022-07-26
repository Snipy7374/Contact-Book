import pymongo
import os

class MyDatabase:
  
  def __init__(self, db_name, collection_name) -> None:
    self.username = os.environ['username']
    self.password = os.environ['password']
    self.db_name = db_name
    self.collection_name = collection_name

  def _get_connection(self):
    client = pymongo.MongoClient(f"mongodb+srv://{self.username}:{self.password}@contactbookdb.lckvbig.mongodb.net/?retryWrites=true&w=majority")
    return client

  def _get_db(self):
    return self._get_connection()[f"{self.db_name}"]

  def _get_collection(self):
    return self._get_db()[f"{self.collection_name}"]

  def insert_doc(self, documents):
    return self._get_collection().insert_one(documents)

  def insert_many_doc(self, ls):
    return self._get_collection().insert_many(ls)

  def find(self, query):
    return self._get_collection().find(query)

  def update_doc(self, query, doc):
    return self._get_collection().update_one(query, doc)

  def replace_doc(self, query, doc):
    return self._get_collection().replace_one(query, doc)

  def delete_doc(self, query):
    return self._get_collection().delete_one(query)

  def delete_many_doc(self, query):
    return self._get_collection().delete_many(query)
