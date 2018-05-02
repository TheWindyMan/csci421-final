from __future__ import absolute_import, unicode_literals,  print_function
# from steganography.steganography import Steganography
from steganography import Steganography
import os
from flask import Flask, request, send_file
import sys
app = Flask(__name__)

@app.route('/')
def intro():
    return('Welcome to the Steganography Webservice')
    
@app.route('/test', methods=['POST'])
#Encode method for flask
#:param request.data: str
#:return: image/jpeg
# curl -X POST -H "Content-Type: text/plain" -d "This is a test" https://secret-key-crypto-thewindyman.c9users.io:8081/test >> test.jpg
def stegano():
    print(request.method)
    path = "cat.jpg"
    output_path = "catencodes.jpg"
    text = request.data
    Steganography.encode(path, output_path, text)
    return send_file(output_path, mimetype='image/jpeg')
    
@app.route('/decode', methods=['POST'])
#Decode method for flask
#:param request.files['image']: image/jpeg
#:return: str
# curl -X POST -F "image=@test.jpg" https://secret-key-crypto-thewindyman.c9users.io:8081/decode
def destegano():
    files= request.files['image']
    secret_text = Steganography.decode(files)
    #print(files, file=sys.stderr)
    return secret_text
    
path = "cat.jpg"
output_path = "catencode.jpg"
text = 'The quick brown fox jumps over the lazy dog.'
Steganography.encode(path, output_path, text)