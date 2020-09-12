import ipfsApi
import json
api = ipfsApi.Client(host='https://ipfs.infura.io', port=5001)
#with open('ipfs.txt') as json_file:
    #abi = json.load(json_file)
new_file = api.add('pe.jpg')
#p=api.cat('QmZqiuTUnSXXM3SUFdZ3mYkHHXh2MyNVTci1aaksv3fsPS')
#p=p.decode("utf-8")
#p=json.loads(p)
#print(p['employee']['name'])
print(new_file)
