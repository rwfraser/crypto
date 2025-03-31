from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from datetime import datetime
from models import CoinModel
from http_status import HttpStatus
from pytz import utc
import sqlite3
import constants
#  CHAUFFE Cloud Manager 

# upon CloudManager start up 1)check for #1 database, if not exist
# then create GenesisBlock database #1. 
#  2) start API server and wait for connection
#  
# Hardcoded GenesisBlock for Controller #1
COLD_START = False 

if COLD_START:
    '''
    On first iteration, create CloudManager database and data for GenesisBlock in first Controller
    '''
    connection = sqlite3.connect('CloudManager.db')
    with sqlite3.connect('CloudManager.db') as connection:
        cursor = connection.cursor()
        print("database created and connected successfully")

        create_table_query = '''
        CREATE TABLE IF NOT EXISTS CloudManager (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        CloudManagerID TEXT NOT NULL,
        Create_Date DATE
        );
        '''

        create_table_query = '''
        CREATE TABLE IF NOT EXISTS GenesisBlock000000001 (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        ControllerID TEXT NOT NULL,
        DLOID TEXT NOT NULL,
        OWNER_NAME TEXT NOT NULL
        OWNER_PRIVATE_KEY
        Create_Date DATE
        );
        '''

        create_table_query = '''
        CREATE TABLE IF NOT EXISTS CoinbaseTransaction000000001 (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        CoinbaseTransactionID TEXT NOT NULL,
        DLOID TEXT NOT NULL,
        RightsByte TEXT NOT NULL,
        Create_Date DATE
        );
        '''

        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        id TEXT NOT NULL,
        input TEXT,
        output TEXT,
        Lock TEXT' \
        ');
        '''
        # cursor.execute(create_table_query)
        connection.commit()
        print("Table 'Transactions' created successfully")
        



# Listen for and parse API commands

# API commands are 
# - wakeup/ack 
# - create Controller  POST localhost:8000\MakeController DLOID="string" varstring=byte
# - create GenesisBlock
# - create CoinbaseTransaction
# - create CHAUFFEcoinTransaction
# - launch BlockChain Explorer



app = Flask(__name__)
service = Api(app)


if __name__ == '__main__':
    #app.run(debug=True)    
    app.run(host='0.0.0.0', debug=True)
