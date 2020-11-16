from eth_account import Account
import json

# create
account = Account.create()
print('private => {0}'.format(account._key_obj))
print('public  => {0}'.format(account._key_obj.public_key))
print('address => {0}'.format(account.address))

# dump
wallet = Account.encrypt(account.privateKey,'123')
wfn = './keystore/{0}.json'.format(account.address)
with open(wfn,'w') as f: 
  json.dump(wallet,f)
print('wallet saved to {0}'.format(wfn))

# load
with open(wfn,'r') as f:
  wallet = json.load(f)
print('wallet loaded from {0}'.format(wfn))
priv_key = Account.decrypt(wallet,'123')
account = Account.privateKeyToAccount(priv_key)
print('private => {0}'.format(account._key_obj))
print('public  => {0}'.format(account._key_obj.public_key))
print('address => {0}'.format(account.address))
