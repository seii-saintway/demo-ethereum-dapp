import requests, time, json
from pprint import pprint

def rpc(method,params=[]):
  print('{0} => '.format(method))
  data = json.dumps({
    'jsonrpc':'2.0',
    'method': method,
    'params': params,
    'id': int(time.time() * 1000)
  })
  rsp = requests.post('http://localhost:8545',data=data)
  pprint(rsp.json())

rpc('web3_clientVersion')
rpc('eth_accounts')




