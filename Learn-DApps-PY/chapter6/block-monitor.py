from web3 import Web3
from web3.utils.encoding import to_hex
import time

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

filter = w3.eth.filter('latest')

while True:
  for hash in filter.get_new_entries():
    print('block hash => {0}'.format(to_hex(hash)))
    block = w3.eth.getBlock(hash)
    print('timestamp => {0}'.format(block.timestamp))
    
  time.sleep(2)
 