from web3 import Web3
from web3.utils.encoding import to_hex

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
accounts = w3.eth.accounts

with open('./the-art-of-war.txt') as f:
  txt = f.read()

data = to_hex(str.encode(txt))

payload = {
  'from': accounts[0],
  'to': accounts[0],
  'data': data
}
estimation = w3.eth.estimateGas(payload)
print('estimated gas usage => {0}'.format(estimation))
