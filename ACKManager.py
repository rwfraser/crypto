from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from datetime import datetime
from http_status import HttpStatus
from pytz import utc
from ACKModels import ACKModel

class ACKManager():
    '''
    ACKManager checks status of CloudManager (online/offline) and responds to MyCHAUFFE.com ACK requests accordingly
    '''
    def __init__(self):
        self.CloudManagerBool = True
        self.creation_date = datetime.now(utc)
        self.ID = 'Cloud Manager ACK v1.0'

    def get_ACK(self,CloudManagerBool):
        '''
        API GET command to /ACKUrl/ returns True if CloudManager is online, False otherwise
        '''
        if self.CloudManagerBool:
            return True
        return False

ACK_fields = {
    'ID': fields.String('Cloud Manager ACK v1.0'),
    'creation_date': fields.DateTime,
    'CloudManagerBool':fields.Boolean(True)
    }

ACK_manager = ACKManager()

class ACK(Resource):
    '''
    Implements API call - GET for ACK
    '''

    @marshal_with(ACK_fields)
    def get(self):
        return ACK_manager

app = Flask(__name__)
CloudManagerACK = Api(app)

CloudManagerACK.add_resource(ACK, '/CloudManagerACK/ACKUrl/')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)
