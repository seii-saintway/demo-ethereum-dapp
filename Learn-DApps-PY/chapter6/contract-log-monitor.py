from web3 import Web3
from pprint import pprint
import time
  
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
accounts = w3.eth.accounts

filter = w3.eth.filter({})

while True:
  for log in filter.get_new_entries():
    pprint(log)
  
  time.sleep(2)