#NOTE: this file was never used
 
#constants that hold the prefex's in the the file that testbs.py generates
WORD_STR = "word: "
W_LEN = len(WORD_STR) 
LINK_STR = "link: "
L_LEN = len(LINK_STR)

file = open('link_record.txt', 'w')

elementList = file.readLines()

for i in range(0,len(elementList)):
    w_index = elementList[i].index(WORD_STR)
    link_index = elementList[i].index(LINK_STR)

    word = elementList[i][w_index+W_LEN]

    
    link = elementList[i][]



file.close()
