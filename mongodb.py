#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:10:16 2018

@author: cheating
"""

from pymongo import MongoClient
import urllib.parse
import datetime

username = urllib.parse.quote_plus('fergus') 
password = urllib.parse.quote_plus('31iwillinto')
host = 'ds155644.mlab.com' #主機位置
port = '55644' #port號碼
dbname='stockbot'
collection='stockbot'

###############################################################################
#                           LineBot股票機器人mongoDB#                            #
###############################################################################

#資料庫連接
def constructor():
    client = MongoClient('mongodb://%s:%s@%s:%s/%s?authMechanism=SCRAM-SHA-1' % (username, password, host, port,dbname))
    db = client[collection]
    return db
   
#----------------------------儲存使用者的股票--------------------------
def write_user_stock_fountion(stock, bs, price):  
    db=constructor()
    collect = db['fountion']
    collect.insert({"stock": stock,
                    "data": 'care_stock',
                    "bs": bs,
                    "price": float(price),
                    "date_info": datetime.datetime.utcnow()
                    })
    
#----------------------------殺掉使用者的股票--------------------------
def delete_user_stock_fountion(stock):  
    db=constructor()
    collect = db['fountion']
    collect.remove({"stock": stock})
    
#----------------------------秀使用者的股票--------------------------
def show_user_stock_fountion():  
    db=constructor()
    collect = db['fountion']
    cel=list(collect.find({"data": 'care_stock'}))

    return cel

