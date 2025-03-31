# stored API commands 
import requests

# wakeup request - 
http GET localhost:5000/cloudmanager/ #returns 200-ok when CloudManager is available

# ******************* record investment in a FULL Controller *************************** 
http POST localhost:5000/cloudmanager/ "DLO_Name"="string", "PrivateKey" = "64 char Hex string", "Type"="GP|LP",  "Rights"=int
# cloudmanager receives the POST command and replies with  200=ok ControllerID, indicating Controller is commissioned and ready for commands
# MYCHAUFFE.com proceeds with GET command with ControllerID parameter
http GET localhost:5000/controller/ControllerID 
# this returns confirmation with Wallet and User Account data: DLOID, ControllerID, CHAUFFEcoin_quantity, TransactionID, rights summary
# *************************************************************************************

# record investment in a PARTIAL Controller *********************************************
http POST localhost:5000/cloudmanager/ "Partial_Name"="string", "PrivateKey" = "64 char Hex string", "Type"="10000|100",  "Rights"=int
# cloudmanager receives the POST command and replies with  200=ok PARTIAL100ID|PARTIAL10000ID, indicating transaction is recorded
# MYCHAUFFE.com proceeds with GET command with PARTIAL100ID|PARTIAL10000ID parameter
http GET localhost:5000/controller/PARTIAL100ID|PARTIAL10000ID  
# this returns confirmation with Wallet and User Account data: PARTIAL100ID|PARTIAL10000ID, CHAUFFEcoin_quantity, TransactionID, rights summary
