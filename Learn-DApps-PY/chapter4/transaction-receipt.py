from web3 import Web3
from web3.utils.encoding import to_hex
import time

def waitForReceipt(tx_hash,timeout=60,interval=2):
  t0 = time.time()
  while(True):
    receipt = w3.eth.getTransactionReceipt(tx_hash)
    if receipt is not None:
      break
    delta = time.time() - t0
    if(delta > timeout ):
      break
    time.sleep(interval)
    
  return receipt

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
accounts = w3.eth.accounts

balance = w3.eth.getBalance(accounts[0],'latest')
print('balance before tx => {0}'.format(balance))

payload = {
  'from': accounts[0],
  'to': accounts[1],
  'value': 100
}
tx_hash = w3.eth.sendTransaction(payload)
print('tx hash => {0}'.format(to_hex(tx_hash)))

receipt = waitForReceipt(tx_hash)
#receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print('gas used => {0}'.format(receipt.gasUsed))

balance = w3.eth.getBalance(accounts[0],'latest')
print('balance after tx => {0}'.format(balance))



