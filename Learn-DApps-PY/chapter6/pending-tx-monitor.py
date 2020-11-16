from web3 import Web3
import time

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

filter = w3.eth.filter('pending')

while True:
  for tx_hash in filter.get_new_entries():
    tx = w3.eth.getTransaction(tx_hash)    
    print('tx data => {0}'.format(tx.input))
      
  time.sleep(2)
 