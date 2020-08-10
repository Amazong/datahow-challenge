import numpy as np

NUM_REQUESTS = 100000

def get_random_timestamp(quot):
    return f'{quot}timestamp{quot}: {quot}2020-06-24T15:27:00.123456Z{quot}'

def get_random_ip(quot):
    return f'{quot}ip{quot}: {quot}%d.%d.%d.%d{quot}' % tuple(np.random.randint(256, size=4))

def get_random_url(quot):
    return f'{quot}url{quot}: {quot}...{quot}'

if __name__ == "__main__":
    # Write vanilla requests to txt file
    json_req = '\n'.join(["{" + \
                ', '.join([get_random_timestamp('"'), get_random_ip('"'), get_random_url('"')]) + \
                "}" \
                for i in range(NUM_REQUESTS)] * 2)
    with open("tests/requests.txt", 'w') as f:
        f.writelines(json_req)

    # Write requests as CSV for use with Postman
    json_req = '\n'.join(["\"{" + \
                ', '.join([get_random_timestamp('""'), get_random_ip('""'), get_random_url('""')]) + \
                "}\"" \
                for i in range(NUM_REQUESTS)] * 2)
    with open("tests/requests.csv", 'w') as f:
        f.write('request\n')
        f.writelines(json_req)

