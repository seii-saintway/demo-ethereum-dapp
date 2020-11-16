from web3 import Web3
from web3.utils.encoding import ( to_hex, to_bytes )
from web3.utils.contracts import encode_abi
from eth_utils.curried import keccak
from eth_abi import decode_single
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

topic = get_topic('Transfer(address,address,uint256)')

opts = {
  'topics': [topic]
}
filter = w3.eth.filter(opts)

while True:
  for log in filter.get_new_entries():
    from_account = decode_single('address',bytes(log['topics'][1]))
    to_account = decode_single('address',bytes(log['topics'][2]))
    value = decode_single('uint256',to_bytes(hexstr=log['data']))
    print('event => Transfer')
    print('  from  : {0}'.format(from_account))
    print('  to    : {0}'.format(to_account))
    print('  value : {0}'.format(value))
  time.sleep(2)