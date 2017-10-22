

#prefex's in the the file that testbs.py generates
WORD_STR = "word: "
W_LEN = len(WORD_STR) 
LINK_STR = "link: "
L_LEN = len(LINK_STR)

file = open('link_record.txt', 'w')

elementList = file.readLines()

for i in range(0,len(elementList)):
    



file.close()
