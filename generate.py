## used to generate the scenarios

import requests
import json

def local_model(q, port=8037):
    url = f"http://127.0.0.1:{port}"
    payload = {'prompt': q}
    out = requests.post(url, json=payload)
    # print(out.text)
    out = json.loads(out.text)
    # print(out) ## 
    return out['result']

def generate(q):
    return local_model(q, port=8037)