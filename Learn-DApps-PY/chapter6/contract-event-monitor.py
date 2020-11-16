from web3 import Web3
import json, time

def load_via_artifact(w3,contract):
  fn_abi = './contract/build/{0}.abi'.format(contract)
  fn_addr = './contract/build/{0}.addr'.format(contract)
  
  with open(fn_abi) as f:
    abi = json.load(f)
    
  with open(fn_addr) as f:
    addr = f.read()
    #modify web3/utils/validation.py
    #see: https://github.com/ethereum/web3.py/issues/730
    addr = addr.lower()  
    
  return w3.eth.contract(address=addr,abi=abi)
  
  
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
accounts = w3.eth.accounts

token = load_via_artifact(w3,'EzToken')

filter = token.events.Transfer.createFilter(fromBlock=0)

while True:
  for event in filter.get_new_entries():
    print('event => {0}'.format(event.event))
    print('  from  : {0}'.format(event.args._from))
    print('  to    : {0}'.format(event.args._to))
    print('  value : {0}'.format(event.args._value))
  
  time.sleep(2)

