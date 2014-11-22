#!usr/bin/local

import urlparse 
import urllib
from bs4 import BeautifulSoup

url ="http://sidgan.tumblr.com"

urls = [url]
#which urls to read 
visited = [url]
#visited sites in chronological order
while len(urls) > 0 : 
	try: 
		text_from_site = urllib.urlopen(urls[0]).read()
	except: 
		print urls[0] #prints entire content of site 
	#converte into beautiful soup 
	soup = BeautifulSoup(text_from_site)
	urls.pop(0)
	print len(urls)

	for tag in soup.findAll('a', href=True):
		tag['href'] = urlparse.urljoin(url, tag['href'])
#		print tag #prints the links that are contained within the page
		if url in tag['href'] and tag['href'] not in visited: 
			urls.append(tag['href'])
			visited.append(tag['href'])

print visited 


