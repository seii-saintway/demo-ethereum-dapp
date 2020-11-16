from web3 import Web3
from web3.utils.encoding import to_hex
from web3.utils.contracts import encode_abi
from eth_utils.curried import keccak
from pprint import pprint
import time,json,sys
  
def load_via_artifact(w3,contract):
  fn_abi = './contract/build/{0}.abi'.format(contract)
  fn_addr = './contract/build/{0}.addr'.format(contract)
  
  with open(fn_abi) as f:
    abi = json.load(f)
    
  with open(fn_addr) as f:
    addr = f.read()
    #modify web3/utils/validation.py
    #see: https://github.com/ethereum/web3.py/issues/730
    #addr = addr.lower()  
    
  return w3.eth.contract(address=addr,abi=abi)
  
def get_topic(text):
  return to_hex(keccak(text=text))
  
def hb_to_hex(hexbytes):
  return to_hex(bytes(hexbytes))
  
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
accounts = w3.eth.accounts

events = {}
topic1 = get_topic('Transfer(address,address,uint256)')
topic2 = get_topic('Approval(address,address,uint256)')
events[topic1] = 'Transfer'
events[topic2] = 'Approval'

opts = {
  'topics': [topic1]
}
filter = w3.eth.filter(opts)

while True:
  for log in filter.get_new_entries():
    topic = hb_to_hex(log['topics'][0])
    print('event => {0}'.format(events[topic]))
      
  time.sleep(2)