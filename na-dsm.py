#!/usr/bin/python
# NetGear Arlo cloud-Downloader for my Synology NAS.
# A. Ramos <aramosf@unsec.net>
# Tue 10 Jan 18:02:18 CET 2017
# ./na-dsm <user> <password>

import cookielib 
import urllib2 
import os, sys
import shutil
try:
    from urllib.request import urlopen # Python 3
except ImportError:
    from urllib2 import urlopen # Python 2
import json
import datetime
import calendar

if len(sys.argv) < 4:
	print "Netgear Arlo downloader"
	print "Usage: na-dsm.py <username> <password> <directory>"
	print "example: na-dsm.py aramosf@unsec.net Zurrupia1 /volume2/share2/"
	sys.exit()

user = sys.argv[1]
password = sys.argv[2]
directory = sys.argv[3]

if not os.path.exists(directory):
	print "Error. Directory: " + directory + " must exist."
	sys.exit(1)

def get_large_file(url, down, length=16*1024):
    req = urlopen(url)
    with open(down, 'wb') as fp:
        shutil.copyfileobj(req, fp, length)


#h=urllib2.HTTPSHandler(debuglevel=1)
#opener = urllib2.build_opener(h)
#urllib2.install_opener(opener)

now = datetime.datetime.now()

req1 = urllib2.Request('https://arlo.netgear.com/hmsweb/devicesupport/v2')
res1 = urllib2.urlopen(req1)
cookie = res1.headers.get('Set-Cookie')
res1.close()

try:
	req2 = urllib2.Request('https://arlo.netgear.com/hmsweb/login')
	req2.get_method = lambda: 'POST'
	creds = ({"email":user, "password":password})
	req2.add_header('cookie', cookie)
	req2.add_header('Content-Type', 'application/json')
	f2 = urllib2.urlopen(req2,json.dumps(creds))
	data2 = json.loads(f2.read())
	cookie2 = f2.headers.get('Set-Cookie')
	f2.close()

except urllib2.HTTPError, e:
	print "Bad password?"
	print 'We failed with error code - %s.' % e.code
	sys.exit(1)

auth = data2['data']['token']
cmonth = now.month
cyear = now.year
days = str(calendar.monthrange(cyear,cmonth)[1])
dfrom = now.strftime("%Y%m01")
dto = now.strftime("%Y%m") + days

req3 = urllib2.Request('https://arlo.netgear.com/hmsweb/users/library')
req3.get_method = lambda: 'POST'
date=({"dateFrom":dfrom,"dateTo":dto})
req3.add_header('cookie', cookie)
req3.add_header('Authorization', auth)
req3.add_header('Content-Type', 'application/json')
f3 = urllib2.urlopen(req3,json.dumps(date))
data3 = json.loads(f3.read())

for vid in data3['data']:
	#print vid
	url = vid['presignedContentUrl']
	utime = int(str(vid['localCreatedDate'])[:10])
	vyear = str(datetime.datetime.fromtimestamp(utime).strftime('%Y'))
	vmonth = str(datetime.datetime.fromtimestamp(utime).strftime('%m'))
	fname = str(datetime.datetime.fromtimestamp(utime).strftime('%Y%m%d_%Hh%Mm%Ss.mp4'))

	if not os.path.exists(directory + "/"+ vyear):
		os.makedirs(directory + "/" + vyear)
	if not os.path.exists(directory + "/" + vyear + "/" + vmonth):
		os.makedirs(directory + "/" + vyear + "/" + vmonth)
	if not os.path.exists(directory + "/" + vyear + "/" + vmonth + "/" + fname):
		downfile = directory + "/" + vyear + "/" + vmonth + "/" + fname
		if not os.path.exists(downfile):
			print "Downloading " + url + " to: " + downfile
			get_large_file(url, downfile)
	

