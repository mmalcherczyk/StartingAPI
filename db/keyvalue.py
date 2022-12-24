import dbm
import argparse
from datetime import datetime

now = datetime.now()
key = now.strftime("%H:%M:%S")

try:
    db = dbm.open("./data/mydb.db", "c")
except ImportError as e:
    print(e)   

# get yaml
def get(args):
    db = dbm.open("./data/mydb.db", "c")
    mdict = {}
    for k, v in (db.items()):
        mdict[k] = v
    return mdict
        
        
def add(args):
    db[key]=args.v

def clear(args):
    db.clear()
     
