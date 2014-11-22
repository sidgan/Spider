#!usr/bin/local
import urlparse 
import urllib
from bs4 import BeautifulSoup
import robotparser

#
#using lynx commands
#lynx -dump http://sidgan.tumblr.com/ > tumblr.txt
#grep 'http://' < tumblr.txt > urls.txt
#obtained edited file urls.txt 
#

url ="http://sidgan.tumblr.com"

u = open('urls.txt', 'r')
first_url = u.readline()

urls = [first_url]
#which urls to read 
visited = [first_url]
#visited sites in chronological order

#make the list of all urls on one site only 

for line in u: 
	urls.append(line)
#created list	
print urls 

#now we need to go and access each one of them
#first check their robot.txt

rp = robotparser.RobotFileParser()
for each in urls: 
	print "Trying to vist " + each
	#sets the url referring to the robots.txt file	
	rp.set_url(each)
	#reads the robots.txt url and feeds it to the parser
	rp.read()
	#returns true if fetching is allowed 	
	if rp.can_fetch("*", each): 
		#go to the site
		print "Gone to the site " + each
		try: 
			text_from_site = urllib.urlopen(urls[0]).read()
		except: 
			print urls[0] #prints entire content of site 
			#converte into beautiful soup 
		soup = BeautifulSoup(text_from_site)
		urls.pop(0)
		print "Number of sites remaining to be crawled " , len(urls)

		for tag in soup.findAll('a', href=True):
			tag['href'] = urlparse.urljoin(url, tag['href'])
#			print tag #prints the links that are contained within the page
			if url in tag['href'] and tag['href'] not in visited: 
				urls.append(tag['href'])
				visited.append(tag['href'])

print visited 
