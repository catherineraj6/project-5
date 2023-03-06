from pymongo import MongoClient
import os
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb


def insert_brevet(brevet_dist, start_time, controls):
    pass

def get_brevet():
    pass

#return the three variables from above