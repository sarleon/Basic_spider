#coding:utf-8
import urllib
import re
import urllib2
import time
import datetime
#currentTime= str(datetime.datetime.now())[0:10]
#currentTime="2016-06-01"
currentTime=str(datetime.datetime.now())[0:10]
print   datetime.datetime.now()
request=urllib2.Request(
    url='https://github.com/torvalds/',
    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'}
)
response=urllib2.urlopen(request)
webpage=response.read()
pattern=re.compile("data-count.*"+currentTime)
match=pattern.search(webpage)
if match:
      line= match.group()
      pattern2=re.compile("\"\d*\"")
      match2=pattern2.search(line)
      print "Linus Torvalds 今天一共push了"+match2.group()+"次"
currentTime=str(datetime.datetime.now())[0:10]
print   datetime.datetime.now()
request=urllib2.Request(
    url='https://github.com/sarleon/',
    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'}
)
response=urllib2.urlopen(request)
webpage=response.read()
pattern=re.compile("data-count.*"+currentTime)
match=pattern.search(webpage)
if match:
      line= match.group()
      pattern2=re.compile("\"\d*\"")
      match2=pattern2.search(line)
      print "你 今天一共push了"+match2.group()+"次"
print "最聪明最优秀最伟大的黑客，程序员，仍然比你更加努力，"