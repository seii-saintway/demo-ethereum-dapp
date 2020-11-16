from eth_account import Account

account = Account.create()

privateKey = account._key_obj
print('private key => {0}'.format(privateKey))

publicKey = privateKey.public_key
print('public key => {0}'.format(publicKey))

address = publicKey.to_checksum_address()
print('address => {0}'.format(address))

