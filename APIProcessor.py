from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from datetime import datetime
from models import GenesisBlockModel, CoinModel, CoinbaseTransactionModel, CHAUFFEcoinTransactionModel
from http_status import HttpStatus
from pytz import utc
from ProtoManager import CoinList, Coin, CoinManager


app = Flask(__name__)
APIProcessor = Api(app)
'''
# wakeup request - 
http GET localhost:5000/cloudmanager/ #returns 200-ok when CloudManager is available

# record investment in a FULL Controller *************************** 
http POST localhost:5000/cloudmanager/ "DLO_Name"="string", "PrivateKey" = "64 char Hex string", "Type"="GP|LP",  "Rights"=int
# get results for Full Controller commissioning
http GET localhost:5000/controller/ControllerID 

# commission a partial investment
http POST localhost:5000/cloudmanager/ "Partial_Name"="string", "PrivateKey" = "64 char Hex string", "Type"="10000|100",  "Rights"=int
# this returns confirmation with Wallet and User Account data: PARTIAL100ID|PARTIAL10000ID, CHAUFFEcoin_quantity, TransactionID, rights summary
http GET localhost:5000/controller/PARTIAL100ID|PARTIAL10000ID  
'''


#obsolete commands
# URL to access ALL Coins
APIProcessor.add_resource(CoinList, '/apiprocessor/coins/')
# URL to access a Coin by ID
APIProcessor.add_resource(Coin, '/apiprocessor/coins/<int:index>',endpoint='coin_endpoint')


if __name__ == '__main__':
    #app.run(debug=True)    
    app.run(host='0.0.0.0', debug=True)
