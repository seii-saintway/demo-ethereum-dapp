from web3 import Web3,Account
from web3.utils.encoding import to_hex
import json

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
accounts = w3.eth.accounts

# load wallet account
wfn = './keystore/{0}.json'.format('0x6FAA97edd198F59DFb6f0063Bc34777eAa0BF02c')
with open(wfn,'r') as f:
  wallet = json.load(f)
priv_key = Account.decrypt(wallet,'123')
account = Account.privateKeyToAccount(priv_key)

# funds wallet account
tx_hash = w3.eth.sendTransaction({'from':accounts[0],'to':account.address,'value':Web3.toWei(1,'ether')})
w3.eth.waitForTransactionReceipt(tx_hash)

balance = w3.eth.getBalance(account.address)
print('wallet balance before raw tx => {0}'.format(balance))

# prepare tx payload
nonce = w3.eth.getTransactionCount(account.address)
payload = {
  'to': accounts[9],
  'value': 1000,
  'gas': 200000,
  'gasPrice': Web3.toWei(20,'gwei'),
  'nonce': nonce,
  'chainId': 1
}
signed = account.signTransaction(payload)
print('signed payload => {0}'.format(to_hex(signed.rawTransaction)))

tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print('gas used => {0}'.format(receipt.gasUsed))

balance = w3.eth.getBalance(account.address)
print('wallet balance after raw tx => {0}'.format(balance))
