import requests
import pymongo
from os import getenv

def count_filter_document():
    client=pymongo.MongoClient(getenv("FILTERS_MONGODB_URI"))
    total_doc=client['Hifi'].records.count_documents({})
    document_count=client['Hifi'].records.count_documents({'status':{'$exists':False}})
    keyword_count=client['Hifi'].records.distinct('keyword')

    API=getenv("TELEGRAM_MESSAGE_API")
    
    API=API.format(
        chat_id=getenv("TELEGRAM_GROUP_CHAT_ID"),
        message="Total documents  : "+str(total_doc)+"\n"+
                "Non-empty Docs   : "+str(document_count)+"\n"+
                "Scraped Keywords : "+str(keyword_count))

    requests.get(API)
    return {
        'status':200,
        'document_count':document_count,
        'total_documents':total_doc,
        'keywords_scraped':keyword_count
        }