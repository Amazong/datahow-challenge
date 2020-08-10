from timeit import default_timer as timer
from datetime import timedelta
import json

unique_ips = set()

def parse_requests(reqs):
    for req in reqs:
        json_req = json.loads(req)
        unique_ips.add(json_req['ip'])

def main():
    with open('tests/requests.txt', 'r') as f:
        reqs = f.readlines()

    start = timer()
    parse_requests(reqs)
    end = timer()
    
    print("Elapsed time:")
    print(timedelta(seconds=end-start), end="\n\n")

    print("Unique IPs seen:")
    print(len(unique_ips), end="\n\n")

    print("Time per request:")
    print(timedelta(seconds=end-start).total_seconds() * 1e9 / len(reqs), end="")
    print(" ns", end="\n\n")

    print

if __name__ == "__main__":
    main()
    