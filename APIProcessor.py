from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from datetime import datetime
from APImodels import FULL
from http_status import HttpStatus
from pytz import utc
from ProtoManager import CoinList, Coin, CoinManager

# http POST localhost:5000/CloudManagerPOST/FULL/ "DLO_Name"="string", "PrivateKey" = "64 char Hex string", "PartnerType"="GP|LP",  "Rights"=int
# http POST localhost:5000/CloudManagerPOST/Partial/ "Partial_Name"="string", "PrivateKey" = "64 char Hex string", "InvestorType"="10000|100",  "Rights"=int

class FULL:
    pass

class Partial:
    pass

app = Flask(__name__)
APIProcessor = Api(app)

APIProcessor.add_resource(POST_FULL, '/CloudManagerPOST/FULL/')
APIProcessor.add_resource(POST_Partial, '/CloudManagerPOST/Partial/')






if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)
