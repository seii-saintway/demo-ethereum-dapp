from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
accounts = w3.eth.accounts

balance = w3.eth.getBalance(accounts[0],'latest')
print('balance@latest => {0}'.format(balance))

balance = w3.eth.getBalance(accounts[0],'earliest')
print('balance@earliest => {0}'.format(balance))

balance = w3.eth.getBalance(accounts[0],0)
print('balance@block#0 => {0}'.format(balance))
