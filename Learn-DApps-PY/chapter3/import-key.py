from eth_account import Account

pk = '0xb25c7db31feed9122727bf0939dc769a96564b2de4c4726d035b36ecf1e5b364'
account = Account.privateKeyToAccount(pk)

privateKey = account._key_obj
print('private key => {0}'.format(str(privateKey)))

publicKey = privateKey.public_key
print('publick key => {0}'.format(str(publicKey)))

address = publicKey.to_checksum_address()
print('address => {0}'.format(address))