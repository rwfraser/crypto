class CoinModel:
    def __init__(self,  CoinID, DLOID, creation_date, quantity, ControllerID):
        self.index = 0                                         # id
        self.CoinID = CoinID                                   # new
        self.DLOID = DLOID                                     # message        
        self.creation_date = creation_date
        self.quantity = quantity                               # ttl        
        self.ControllerID = ControllerID                       # notification_category
