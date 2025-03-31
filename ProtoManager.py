from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from datetime import datetime
from obsoleteModels import  CoinModel
from http_status import HttpStatus
from pytz import utc


class CoinManager():
    '''
    Manages the CoinManager methods and list of Coin fields/attributes
    Initializes the empty chain of coins
    '''
    last_coin_id = 0
    def __init__(self):
        self.coins = {}

    def insert_coin(self, coin):
        self.__class__.last_coin_id += 1
        coin.index = self.__class__.last_coin_id
        self.coins[self.__class__.last_coin_id] = coin

    def get_coin(self, index):
        return self.coins[index]

    def delete_coin(self, index):
        del self.coins[index]

coin_fields = {
    'index': fields.Integer,
    'CoinID': fields.String,
    'uri': fields.Url('coin_endpoint'),
    'DLOID': fields.String,
    'quantity': fields.Integer,
    'creation_date': fields.DateTime,
    'ControllerID': fields.String
}

# instantiate coin_manager object
coin_manager = CoinManager()


class Coin(Resource):
    '''
    Implements API calls - GET, DELETE, PATCH for individual coins
    '''
    def abort_if_coin_not_found(self, index):
        if index not in coin_manager.coins:
            abort(
                HttpStatus.not_found_404.value, 
                message="Coin {index} not found")

    @marshal_with(coin_fields)
    def get(self, index):
        self.abort_if_coin_not_found(index)
        return coin_manager.get_coin(index)

    def delete(self, index):
        self.abort_if_coin_not_found(index)
        coin_manager.delete_coin(index)
        return '', HttpStatus.no_content_204.value

    @marshal_with(coin_fields)
    def patch(self, index):
        self.abort_if_coin_not_found(index)
        coin = coin_manager.get_coin(index)
        parser = reqparse.RequestParser()
        parser.add_argument('CoinID', type=str)
        parser.add_argument('DLOID', type=str)
        parser.add_argument('quantity', type=int)
        parser.add_argument('ControllerID', type=str)
        args = parser.parse_args()
        print(args)
        if 'CoinID' in args and args[CoinID] is not None:
            coin.CoinID = args['CoinID']
        if 'DLOID' in args and args['DLOID'] is not None:
            coin.DLOID = args['DLOID']
        if 'quantity' in args and args['quantity'] is not None:
            coin.quantity = args['quantity']
        if 'ControllerID' in args and args['ControllerID'] is not None:
            coin.ControllerID = args['ControllerID']
        return coin


class CoinList(Resource):
    '''
    Implements API calls - GET (all messages), POST (new message)
    '''
    @marshal_with(coin_fields)
    def get(self):
        return [v for v in coin_manager.coins.values()]

    @marshal_with(coin_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('CoinID', type=str, required=True, help='CoinID cannot be blank!')
        parser.add_argument('DLOID', type=str, required=True, help='DLOID cannot be blank!')
        parser.add_argument('quantity', type=int, required=True, help='quantity cannot be blank!')
        parser.add_argument('ControllerID', type=str, required=True, help='ControllerID cannot be blank!')

        args = parser.parse_args()
        coin = CoinModel(
            CoinID=args['CoinID'],
            DLOID=args['DLOID'],
            quantity=args['quantity'],
            creation_date=datetime.now(utc),
            ControllerID=args['ControllerID']
            )
        coin_manager.insert_coin(coin) 
        return coin, HttpStatus.created_201.value
