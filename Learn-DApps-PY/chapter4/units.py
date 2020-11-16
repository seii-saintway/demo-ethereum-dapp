from web3 import Web3

gwei20 = Web3.toWei(20,'gwei')
print('20 gwei = {0} wei'.format(gwei20))

wei5200 = Web3.fromWei(5200,'ether')
print('5200 wei = {0} ether'.format(wei5200))