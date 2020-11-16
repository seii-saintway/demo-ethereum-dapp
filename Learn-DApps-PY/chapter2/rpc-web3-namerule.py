from web3 import Web3, HTTPProvider
from web3.eth import Eth
from pprint import pprint

w3 = Web3(HTTPProvider('http://localhost:8545'))
eth = Eth(w3)

pprint(eth.accounts)
print('gas price => {0}'.format(eth.gasPrice))