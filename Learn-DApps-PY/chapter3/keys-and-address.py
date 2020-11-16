from eth_keys import keys
from eth_utils.curried import keccak
import os, codecs

def to_hex(raw):
  return '0x' + codecs.decode(codecs.encode(raw, 'hex'), 'ascii')

key_bytes = keccak(os.urandom(32) + b'some entropy you want')
print('{0:>18} => {1}'.format('raw key',to_hex(key_bytes)))

privateKey = keys.PrivateKey(key_bytes)
print('{0:>18} => {1}'.format('private key',str(privateKey)))

publicKey = privateKey.public_key
print('{0:>18} => {1}'.format('public key',str(publicKey)))

address = publicKey.to_checksum_address()
print('{0:>18} => {1}'.format('checksum address',address))
