#HOW TO READ AND WRITE FROM FILES(23)
# #First we create a file(Writing)
# fw = open('sample.txt','w')
# #Here we then write into the file
# fw.write("What is the capital city of Kenya\n")
# fw.write("Nairobi\n")
# #We then close the file to free extra memory
# fw.close()
#
# #Reading from a file
# #First, we create a variable for reading and file to read from
# fr = open('sample.txt','r')
# #Store what to read in a variable
# text = fr.read()
# #print output
# print(text)
# #close to free extra memory
# fw.close()


#DOWNLOADING FILES FROM THE WEB
from urllib import request
goog_url ='https://www.kaggle.com/camnugent/sandp500'

