import requests
import re

HOST = '10.129.10.191'
USER = 'fergus'

def init session():
    # Return CSRF + Session (cookie)
    r = requests.get('http://10.10.10.191/admin/')
    csrf = re.search(r'input type="hidden" id="jstokenCSRF" value="([a-f0-9]*)", r.text')
    csrf = csrl.group(1)
    return csrf    

print (init_session())


