from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
accounts = w3.eth.accounts
balance = w3.eth.getBalance(accounts[0])
print('balance => {0}'.format(balance))