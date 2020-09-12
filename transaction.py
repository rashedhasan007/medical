from web3 import Web3
from web3 import Web3, middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
import json
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.setGasPriceStrategy(medium_gas_price_strategy)

account_1 = '0x77d22712b117375a33A5c7f50cf5B3B69383c144' # Fill me in
account_2 = '0x006133a7872019dAD81BD706eB010F4D0A6d29b4' #account_1 = '' # Fill me in

private_key = 'cde32be4a117ca962d3fb731edfddf9038a389387efb0b1d02b3d0263b7e8b2f' # Fill me in

abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))