from web3 import Web3
import json, time

def load_via_artifact(w3,contract):
  fn_abi = './contract/build/{0}.abi'.format(contract)
  fn_addr = './contract/build/{0}.addr'.format(contract)
  
  with open(fn_abi) as f:
    abi = json.load(f)
    
  with open(fn_addr) as f:
    addr = f.read()
    
  return w3.eth.contract(address=addr,abi=abi)

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
accounts = w3.eth.accounts

token = load_via_artifact(w3,'EzToken')

while True:
  token.functions.transfer(accounts[1],1).transact({'from':accounts[0]})  
  balance = token.functions.balanceOf(accounts[1]).call()
  print('balance => {0}'.format(balance))
  time.sleep(3)