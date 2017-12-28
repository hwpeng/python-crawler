from __future__ import print_function
import sys
import urllib
import urllib2
import re


key_word = sys.argv[1]
conf = sys.argv[2]
year = sys.argv[3]



url_base = "http://dblp.uni-trier.de/db/conf/"

url = url_base+conf+"/"+conf+year+".html"

try:
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	content = response.read()
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print(e.code)
	if hasattr(e,"reason"):
		print(e.reason)

pattern = re.compile('<div class="data" itemprop="headline">(.*?)</div>')

items = re.findall(pattern,content)

i=1
for item in items:
	if re.search(key_word,item,re.IGNORECASE):
		print(i, end='\n')
		authors = re.findall(re.compile('<span itemprop="name">(.*?)</span>'),item)
		for author in authors:
			print(author, end=', ')
		print(' ')
		title = re.findall(re.compile('<span class="title" itemprop="name">(.*?)</span>'),item)
		print(title[0], end='\n')
		i=i+1
		print(' ')
