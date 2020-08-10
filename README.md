# DataHow Backend Intern Coding Challenge

Total time invested: ~5 hours

## Overview

In this challenge I was asked to design a micro-service with REST API to display the number of unique IPs observed during the service's runtime.

This implementation is functionally complete, and accomplishes all the stated requirements.

## Usage

It is possible to run the server by running the command `python run_server.py` from the root folder.

If necessary, the required dependencies can be installed in a virtual environment using the following commands:
```bash
virtualenv my_env
source my_env/bin/activate
pip install -r requirements.txt
```

## Implementation

The micro-service was written using the Flask framework. The main logic for this can be found in the file `app/count_unique_ips.py`.

This file includes four main components:

1. **`parse_json`** parses the incoming JSON requests. Given a JSON-formatted request, this function extracts the corresponding IP and adds it to the list of previously-seen *unique* IPs.
2. **`unique_ip_count_as_json`** returns a JSON-formatted string with the number of unique previously-observed IPs.
3. **`receive_json`** listens for incoming POST requests.
4. **`get_unique_ip_count`** displays the result of `unique_ip_count_as_json` in response to a GET request.

The key idea here is to use of a Python ```set()```, which implements a hash table, to keep track of the previously-seen IPs as strings. This allows average O(1) time for checking of existing IP addresses and insertion of new IP addresses, in O(N) space. In addition, the set class automatically manages deduplication transparently and efficiently.

As can be seen in the local test, on my machine it takes ~2.5us to perform each table update with 200000 requests and 100000 unique IPs.

### Libraries

* **Flask:** Web framework used to write the microservice.
* **JSON:** Used to parse the incoming requests, as well as to display the number of unique IPs.
* **Numpy:** Used for vectorised random number generation for testing.

## Testing
Two tests were performed during development:
* A local test. This was done to validate the algorithmic efficiency of the implementation. This test can be reproduced by running the script `tests/test_local.py`.
* A server test. To perform this, I used Postman: the associated collection is provided under `DataHow-Challenge.postman_collection.json`, and the CSV with requests is under `tests/requests.csv`. This CSV can be regenerated with the script `generate_requests.py`. Postman reported ~3ms to serve each request using the default parameters for the execution of the server running Flask.
