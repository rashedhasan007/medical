from web3 import Web3, HTTPProvider
import json
import web3
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/7b834d2b1f444e6c948553401da3c98f"))
from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
w3.isConnected()

my_account = w3.eth.account.create('Nobody expects the Spanish Inquisition!')
print(my_account._address)
a=my_account._private_key
print(Web3.toHex(a))
print(w3.eth.accounts.privateKeyToAccount(Web3.toHex(a)))
