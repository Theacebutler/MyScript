import requests

url = 'https://10.39.3.1:4100/wgcgi.cgi'

ctx = {
    "fw_username": 'abutler',
    'fw_password': 'icyE@rth99',
    'fw_domain:': "Firebox-DB",
    'action': "fw_logon",
    'fw_logon_type': "logon",
    'redirect': '', 
    'lang': 'en-US'
}

try:
    res = requests.post(url, json=ctx, verify=False)

    res.raise_for_status()
    with open('h.html', 'w') as F:
        F.write(str(res.content))
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
