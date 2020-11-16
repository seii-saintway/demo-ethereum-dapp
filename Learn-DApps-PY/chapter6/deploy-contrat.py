from web3 import Web3
from web3.utils.encoding import to_hex
import json

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
accounts = w3.eth.accounts

artifact = 'EzToken'

fn_abi = './contract/build/{0}.abi'.format(artifact)
fn_bin = './contract/build/{0}.bin'.format(artifact)
fn_addr = './contract/build/{0}.addr'.format(artifact)

with open(fn_abi,'r') as f:
  abi = json.load(f)

with open(fn_bin,'r') as f:
  bin = json.load(f)

factory = w3.eth.contract(abi=abi,bytecode=bin)

txhash = factory.constructor(1000000000,'HAPPY COIN',0,'HAPY').transact({'from':accounts[0]})
print('deploy tx hash => {0}'.format(to_hex(txhash)))

receipt = w3.eth.waitForTransactionReceipt(txhash)
print('deplyoed adress => {0}'.format(receipt.contractAddress))

with open(fn_addr,'w') as f:
  f.write(receipt.contractAddress)
print('contract address saved => {0}'.format(fn_addr))  


