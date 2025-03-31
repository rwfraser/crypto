# set required Constants
# Genesis Block #1-9000 strings
# 
# up to 10,000 controllers will be initially commissioned  
# Genesis Block, Coinbase Transaction and First Transaction objects
# 
ControllerID = ""
OWNER_NAME = "CHAUFFE LLLP"

class GenesisBlock:
    '''
    Genesis Block anchors the BlockChain and identifies with ControllerID, DLOID, Owner Name, DLO Name
    ControllerPriority, 
    '''
    
    def __init__(self, OWNER_NAME, DLO_NAME, ControllerNum, ControllerPriority):
        self.OWNER_NAME = OWNER_NAME
        self.DLO_NAME = DLO_NAME
        self.ControllerNum = ControllerNum
        self.ControllerPriority =  ControllerPriority

    def makeGenesisBlock(self):
        '''
        Create the Genesis Block for a given Controller, and DLO
        '''
        DLOID = sha256(DLO_NAME) 
        CONTROLLER_ID = sha256(CONTROLLER_ID)

class CoinbaseTransaction():
    '''
    Issue currency - typically 100,000 coins per Controller
    '''
    # Coinbase Transaction Constants 
    DEFAULT_QUANTITY = 100000  #100,000 coins issued in Coinbase Transaction except Indiegogo level investors



    

 
    # locate any non-zero var and convert accordingly