from flask import Flask, render_template, request
from werkzeug import secure_filename
import json
import ipfsApi
api = ipfsApi.Client(host='https://ipfs.infura.io', port=5001)
app = Flask(__name__,template_folder='template')
with open('ipfs.txt') as json_file:
    abi = json.load(json_file)
@app.route('/upload')
def upload_file():
   return render_template('uploader.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      print(f)
      new_file = api.add(f)
      print(new_file)
      abi['patient'].append(new_file['Hash'])
      print(abi)
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run()