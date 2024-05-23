import os
# Import the custom encoder class using the alias "encoder"
from pymongo import MongoClient
from dotenv import load_dotenv
import ast
from bson.json_util import dumps
import logging
from datetime import datetime
import sys


def mongo_query():
    try:
        # Mongo Import
        input_query = {'content.TransactionID':'WBZ123'}
        projection = {'content.Invoice_File_ID':1,'_id': 0}
        load_dotenv()
        #input_query=ast.literal_eval("{"+input_query+"}")        
        client = MongoClient('192.168.110.135', 27017)
        #my_client = MongoClient(os.environ.get('MONGO_STRING'))

        # database and collection
        #db = my_client[os.environ.get('MONGO_CLIENT')]
        #collection = db[os.environ.get('MONGO_COLLECTION')]
        mydatabase = client.InvoiceBotz
        collection_name = mydatabase.Invoices
        q_results = collection_name.find(input_query,projection)

        l_results= list(q_results)
        json_data = dumps(l_results, indent = 2)       
        
        with open('data.json','w') as file:
            file.write(json_data)
        #print(json_data)
        return(dumps(l_results))
    except Exception as e:        
        sys.exit(str(e))