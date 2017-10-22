import time 
from bs4 import BeautifulSoup 

import urllib

#constants
websiteBaseURL = "https://www.handspeak.com"
SLEEPTIME = 5

#For now foo, this method will just return the first link whose video tag has the attr id="mySign"
# In the 2 links I checked, there should just be just 1 video tag with that attr value, but whoo nose...  (because there are 5000+ links)
def extractVidLinks(soup):
	vidTag = soup.find_all("video",id="mySign")[0] #get the first element of the set of matched elements 
	return [ websiteBaseURL + vidTag['src'] ]


flag = True
i = 1

wordStore = [] 
linksStore = []
file = open('link_record.txt', 'w')

while flag and i<10:

	r = urllib.urlopen('https://www.handspeak.com/word/search/index.php?id='+str(i)).read()
	soup = BeautifulSoup(r,"html.parser")

	#print(type(soup))
	#print(soup.prettify())

	wordTags = soup.find_all('span', itemprop="name")

	prefix = "ASL sign for: "

	if len(wordTags) > 1:
		print "EWRROR: there should be only one tag where <span itemprop='attr' " 
		quit()
	elif len(wordTags) < 1:	
		print "There is no tag where <span itemprop='attr' ...> "
		flag = False 
	else: #if true then len(wordTags) = 1
		wLen = len(wordStore)
		lLen = len(linksStore)

		contents = wordTags[0].string
		begInd = contents.index(prefix)
		word = contents[begInd+len(prefix):]
		linksStore.append(extractVidLinks(soup))
		
		#print str(i) + ": " + word + "  link: " + linksStore[i-1][0]

		print str(i) + ": " + word
		wordStore[wLen:wLen] =  [word]
		i += 1
		if i%100==0:
			print "Sleeping for " + str(SLEEPTIME) + " miliseconds"
			time.sleep(SLEEPTIME)




for i in range(0,len(wordStore)): 
	entry = 'word: ' + wordStore[i] + "  link: " + linksStore[i][0] 
	print entry
	file.write(entry+"\n")

file.close()	

		#print "span tag: " +  word

		

		


