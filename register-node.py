import os, json, requests, logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(pathname)s %(asctime)s %(levelname)s %(message)s',
    filename=__file__.replace('.py', '.log'),
)

s = os.popen('ip.cmd').read()
j = json.loads(s)
j['ip_address'] = j['ip_address'].strip()
j['mac_address'] = j['mac_address'].strip()

logging.info(f"Registering new node {j}")

headers = {'AUTHORIZATION': 'secret'}
r = requests.post("http://localhost:8000/api/v1/whitelist/node", headers=headers, data=j)
logging.info(r.json())
