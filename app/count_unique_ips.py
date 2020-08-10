import json
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# Set where the IPs will be stored, as strings, as they are received
unique_ips = set()


def parse_json(json_req):
   """Adds the IP from a received request to the set of previously-seen IPs"""

   json_req = json.loads(json_req)
   unique_ips.add(json_req['ip'])

   return json_req['ip']


def unique_ip_count_as_json():
   """Returns the total number of unique IPs as a JSON-formatted string"""

   unique_ip_count = {
      "unique_ips": len(unique_ips)
   }
   
   return json.dumps(unique_ip_count)


@app.route('/')
def main():
   """Placeholder text for the server root"""

   return "Hello, DataHow!"


@app.route('/logs', methods = ['POST', 'GET'])
def receive_json():
   """Implementation of /logs.
   
   This listens for incoming POST requests on port :5000.
   When a request is received, the incoming JSON is parsed using the function parse_json.
   """

   if request.method == 'POST':
      return parse_json(request.data)
   else:
      return 'Please submit your logs using POST requests.'


@app.route('/visitors')
def get_unique_ip_count():
   """Implementation of /visitors.
   
   This returns a single JSON object containing:
   {"unique_ips", # of unique IPs seen}
   """
   return unique_ip_count_as_json()


if __name__ == '__main__':
   """ Main """
   app.run(debug=True, port=5000, threaded=True)
