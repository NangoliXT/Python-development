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

# print(text)
# #close to free extra memory
# fw.close()


#DOWNLOADING FILES FROM THE WEB
# from urllib import request
# #The url is stored in a variable goog_url
# goog_url ='https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1588152907&period2=1619688907&interval=1d&events=history&includeAdjustedClose=true'
#
# #A function is defined to download stock data
# def download_stock_data(csv_url):
# #A connection to the internet is formed
#     response = request.urlopen(csv_url)
# #Reading what is in the accessed file
#     csv = response.read()
#     #Converting data to string
#     csv_str = str(csv)
# #create variable variable that will store the split data
#     lines = csv_str.split("\\n")
# #the variable is used to store the new url
#     dest_url = r'goog.csv'
#
# #The file is open and written to
#     fw = open(dest_url, 'w')
# #a for loop is used to write data in the file
#
#     for line in lines:
#
#        fw.write(line + '\n')
#     fw.close()
#
# download_stock_data(goog_url)

##---------------------------------------------------------------------------------------------------
##---------------------------------------------------------------------------------------------------

#HOW TO BUILD A WEB CRAWLER
#----------------------------------------------------------------------------------------------------

#This helps to create a connection to the internet#

#import requests
#Define the spider that will crawl through the web pages
#def trade_spider(max_pages):
#The page is first set to one for testing and eventually set to as many pages as possible
  #  page = 1
# The while loop will loop through the first page to the pages equal to max_pages
  #  while page <= max_pages:
#The URL address that will be crawled
   #     url = 'https://www.emf-health.uon-powernet.com/index.php'+ str(page)

#Create a variable in which whenever its crawling of various pages it is stored in that variable

 #       source_code = requests.get(url)
#We create a variable that will hold the text accessed through the url
  #      plain_text = source_code.text
#An object is created to access Beautiful soup
  #      soup = BeautifulSoup(plain_text)
#The for loop is used to interate through the page collect all information needed
 #       for link in soup.findAll('a',{'class':'dropdown-item'}):
  #          href = link.get('href')
 #           print(href)

#trade_spider(1)

#--------------------------------CLASSES AND OBJECTS---------------------------
# class Enemy: #Class is given a name enemy#
#      life = 3 #Each enemy is given 3 lifes
#
#      def attack(self):#Create a variable that will signify an attack
#           print('Ouch!')
#           self.life-=1# One life everytime there will be an attack
#
#      def CheckLife(self):#This function checks for life in an enemy
#           if self.life <=0:
#                print('I am dead') #prints out dead if the enemy is dead
#           else:
#                print(str(self.life)+'life left')#prints out the amount of life left
#
# enemy1= Enemy()# An object enemy1 is created to access the class
# enemy2 = Enemy()
# enemy1.attack()#This helps in accessing the function attack inside the class
# enemy1.attack()# Enemy1 attacked the second time
# enemy1.CheckLife()#This helps access the life status of the enemy
# enemy2.CheckLife()#Displays the amount of life enemy 2 has


#-----------------------INIT FUNCTION------------------------------------------

# class Enemy:
#
#      def __init__(self, x): # This function gets implemented even when not called initially
#
#          self.energy = x # The variable x is declared in the class inside a function
#
#      def get_energy(self):# This function is used to display the various values given to x
#           print(self.energy)
# jason = Enemy(5)# An object called jason is created with x being assigned as 5
# Sandy = Enemy(18)# An object called Sandy is created with energy level x assigned as 18
# jason.get_energy()# It displays the energy level of jason
# Sandy.get_energy()# It displays the energy level of Sandy


#-----------------------------CLASSES VS INSTANCE VARIABLES---------------------------------

# class Girl: # a class called girl is created
#     gender = 'female'# A class variable or class default variable is created
#
#     def __init__(self, name):# An instantatious function is created
#         self.name = name# An instance variable is created.
#
# r = Girl('Nicole')# An object given the NICOLE name is created
# s = Girl('Immy')#An object given the Immy name is created
# print(r.gender)#Dislays the gender declared to r
# print(s.gender)#Dislays the gender declared to s
# print(r.name))#Dislays the name declared to r
# print(s.name))#Dislays the name declared to s
# #

#---------------------------------INHERITANCE----------------------------------------------

# class Parent():# a parent class is created
#     def print_last_name(self):# The function that displays the parents' last name is craeted
#         print('Magona')
# class Child(Parent):# The class child is created
#     def print_first_name(self):#The function that displays first name of the child is created
#         print('Nangoli')
#
#     def print_last_name(self):# This function overwrites the name inherited from parent
#         print('Pascal')
# p= Child()# A child object is created
# p.print_first_name()#It displays the first name of the child as Nangoli
# p.print_last_name()#It displays the inherited last name
#









