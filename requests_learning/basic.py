import requests
r=requests.get("http://sarleon.top/")
print type(r)
print r.encoding
print r.status_code
#print r.text
#print r.content
print r.cookies