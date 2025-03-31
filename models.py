class CloudManagerWakeModel:
    def __init__(self, ID):
        self.ID = ID
        self.creation_date = creation_date

class CoinModel:
    def __init__(self,  CoinID, DLOID, creation_date, quantity, ControllerID):
        self.index = 0                                         # id
        self.CoinID = CoinID                                   # new
        self.DLOID = DLOID                                     # message        
        self.creation_date = creation_date
        self.quantity = quantity                               # ttl        
        self.ControllerID = ControllerID                       # notification_category
        
        
class GenesisBlockModel:
    def __init__(self, DLOID, ControllerID):
        self.DLOID = DLOID
        self.ControllerID = ControllerID

class CoinbaseTransactionModel:
    def __init__(self, quantity, collateralizable=False, convertible=0, revenue_sharing=False, redeemable='N'):
        self.quantity = quantity
        self.collateralizable = collateralizable
        self.convertible = convertible
        self.revenue_sharing = revenue_sharing
        self.redeemable = redeemable

class CHAUFFEcoinTransactionModel:
    def __init__(self, version, input, output, locktime):
        self.version = version
        self.input = input
        self.output = output
        self.locktime = locktime 
        
