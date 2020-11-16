from web3 import Web3
from web3.utils.encoding import to_hex
import time

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

filter = w3.eth.filter('latest')

while True:
  for blk_hash in filter.get_new_entries():
    block = w3.eth.getBlock(blk_hash,True)
    for tx in block.transactions:
      print('tx data => {0}'.format(tx.input))
      
  time.sleep(2)
 