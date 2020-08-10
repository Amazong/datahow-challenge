import json

from flask import Flask
from flask import render_template
from flask import request
from flask import Flask, redirect, url_for, request

# Alternative server
#from waitress import serve

app = Flask(__name__)

unique_ips = set()

def parse_json(json_req):
   json_req = json.loads(json_req)
   unique_ips.add(json_req['ip'])
   return json_req['ip']

def unique_ip_count_as_json():
   unique_ip_count = {
      "unique_ips": len(unique_ips)
   }
   
   return json.dumps(unique_ip_count)

@app.route('/')
def main():
    return "Hello, DataHow!"

@app.route('/logs', methods = ['POST', 'GET'])
def receive_json():
   if request.method == 'POST':
      return parse_json(request.data)
   else:
      return 'Please submit your logs using POST requests.'

@app.route('/visitors')
def login():
   return unique_ip_count_as_json()

if __name__ == '__main__':
   app.run(debug=True, port=5000, threaded=True)
   #serve(app, host="localhost", port=5000)
