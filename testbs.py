from bs4 import BeautifulSoup 

import urllib

flag = True
ind = 1

wordStore = [] 



while flag and ind<10: 

	r = urllib.urlopen('https://www.handspeak.com/word/search/index.php?id='+str(ind)).read()
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
		contents = wordTags[0].string
		begInd = contents.index(prefix)
		word = contents[begInd+len(prefix):]
		
		print str(ind) + ": " + word 
		wordStore[len(wordStore):len(wordStore)] =  [word]
		ind += 1

print wordStore



		#print "span tag: " +  word

		

		


