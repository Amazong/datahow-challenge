from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

unique_ips = set()

@app.route('/')
def main():
    return "Hello, world!"

@app.route('/logs')
def receive_json():
   return 'Logs'

@app.route('/visitors', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      return 'Visitors POST'
   else:
      return 'Visitors GET'

if __name__ == '__main__':
   app.run(debug=True, port=5000)