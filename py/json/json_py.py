import json
import requests
data = {'test': 'Hello'}
data_json = json.dumps(data)
r = requests.get('http://localhost:8069/test/result', data=data_json)