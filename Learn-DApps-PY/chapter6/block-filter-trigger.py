from web3 import Web3
from web3.utils.encoding import to_hex
import time

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
accounts = w3.eth.accounts

while True:
  tick = int(time.time()*1000)
  txhash = w3.eth.sendTransaction({'from':accounts[0],'to':accounts[1],'value':1,'data': to_hex(tick)})
  w3.eth.waitForTransactionReceipt(txhash)
  
  balance = w3.eth.getBalance(accounts[0])
  print('balance => {0}'.format(balance))
  
  time.sleep(3)