import urllib
import urllib2

values={"username":"xxxxxxxxxxx","password":"xxxxxxxxxx"}
data=urllib.urlencode(values)
url="http://219.219.114.172/portal_io/login"
headerValue={
     "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
     "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",

 }
headers=urllib.urlencode(headerValue)
request=urllib2.Request(url,data)
response=urllib2.urlopen(request)
jsonMessage=response.read()
print  jsonMessage