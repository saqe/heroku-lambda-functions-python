import requests
import pymongo
from os import getenv

def count_filter_document():
    client=pymongo.MongoClient(getenv("FILTERS_MONGODB_URI"))
    document_count=client['Hifi'].records.count_documents({'status':{'$exists':False}})
    return {
        'status':200,
        'document_count':document_count}
