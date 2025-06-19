# String datatype :-
    #String is sequence of character
    #String is an immutable datatype --> immutable = which cannot be modified once created
    #String is an Ordered Datatype --> it's support indexing
    # String must initialized inside quotes
      #single quotes --> ''
      #double quotes --> ""
      #tripple single quotes --> ''' '''
      #triple double quotes --> """ """

# x = 5
# y = 6.5
# z = 3-7j

#Initalizing

# m = 'hyderabad'

# EXAMPLES OF INTIALIZING STRING :-

# str_1 = 'python'
# print(str_1)
# print(type(str_1))  #< class 'str'>

# str_2 = "Angular"
# print(str_2)
# print(type(str_2))

# str_3 = '''MS SQL SERVER'''
# print(str_3)
# print(type(str_3)) 

# str_4 = """Django"""
# print(str_4)
# print(type(str_4))

# 'Sujith is the 'tallest' among all the classmate'  --> throws error
# "Sujith is the 'tallest' among all the classmate"
# 'Sujith is the '''tallest among all''' the classmate'
# We should different quotes in a single string

# str_6 = 'ameerpet'
# str_7 = "Punjagutta"
# str_8 = ''' This is a python class, class starts at 9am IST'''

# METHODS :-
  #Methods are nothing but functions where the program/code/functionality is defined
  # Built in methods
  # User defined methods
  
 # Some BUILT IN METHODS of string
   
   # CASE CONVERSION METHODS :-
       # this method impy upon only those charecters which 
       # are alphbetic in string
       # str_9 = 'SAM@123'
       
# str_10 = 'jamaica'
# print(str_10.lower()) #jamica
# print(str_10.upper())  #JAMICA

# str_11 = "INDIA"
# print(str_11.lower())  #india
# print(str_11.upper())   #INDIA

# str_12 = 'sam@123'
# print(str_12.lower())  #sam@123
# print(str_12.upper())  #SAM@123

# str_13 = '''india is my country, all indians are my brothers.'''
# print(str_13.lower())  #india is my country, all indians are my brothers.
# print(str_13.upper())   #INDIA IS MY COUNTRY, ALL INDIANS ARE MY BROTHERS.
# print(str_13.capitalize())  #India is my country, all indians are my brothers.
# print(str_13.title())  #India Is My Country, All Indians Are My Brothers.

# str_14 = 'aPplE a DAy kEEpS DoctoR AWay'
# print(str_14.swapcase())   #ApPLe A daY KeePs dOCTOr awAY

##########################

# Indexing of two types 
 # Positive indexing starts with zero 
  # It's starts from left to right
 # Negative indexing starts from -1
  # starts from right

# SEARCH AND REPLACE METHODS

# str1 = 'Hello Buddy, This is Shiv her, luck..!'

#find()
# print(str1.find('B'))
# print(str1.find('Z'))
# print(str1.find('l'))

# rfind()
# # print(str1.rfind('l'))
# print(str1.rfind('k'))
# print(str1.rfind('j'))

# # index()
# print(str1.index('B'))
# print(str1.index('l'))
# print(str1.index('z'))  #ValueError: substring not found

# rindex()
# print(str1.rindex('l'))
# print(str1.rindex('w')) ValueError: substring not found

# replace()
# str2 = 'Apple A Day Kepps Doctor Away'
# print(str2.replace('A', 'a'))
# print(str2)

##############################
# CHECKING CONTENT

# str3 = 'My Dear Friend'

# # strtswith()
# print(str3.startswith('My')) #True
# print(str3.startswith('my')) # Flase
# print(str3.startswith('My  Dear')) # Flase
# print(str3.startswith('My Dea')) # True
# print(str3.startswith(' My Dear')) # Flase
 
# endswith()
# print(str3.endswith('My Dear')) # Flase
# print(str3.endswith('end'))  # True
# print(str3.endswith('Friend'))
# print(str3.endswith('My Dear Friend')) # True

# isalpha()
# str1 = 'grapes'
# print(str1.isalpha())

# str2 = 'Grapes'
# print(str2.isalpha())

# str3 = 'Grape@'
# print(str3.isalpha())

# str4 = 'Grape12223'
# print(str4.isalpha())

# str5 = 'Grapes@123'
# print(str5.isalpha())

# isdigit()
# str11 = '12345'
# print(str11.isdigit())

# str12 = 'g@123'
# print(str12.isdigit())

# str13 = '123.45'
# print(str13.isdigit())

# str14 = '12 23 34 56'
# print(str14.isdigit())

# isalumn()

# str15 = '123456qwert'
# print(str15.isalnum())

# str16 = 'Ganesh@123'
# print(str16.isalnum())

# str17 = '123456789'
# print(str17.isalnum())

# str18 = 'asdfghj'
# print(str18.isalnum())

# isspace()
# str19 = ' '
# print(str19.isspace())

# # islower()
# str20 = 'assdfjglksdjf'
# print(str20.islower())

# str21 = 'asdfghj234'
# print(str21.islower())

# str22 = 'qwerewr@123'
# print(str21.islower())

# str23 = 'ASDSF'
# print(str23.islower())

# str24 = 'FADFAFD'.lower()
# print(str24.islower())

# str25 = 'sdfdsfs'.upper()
# print(str25.islower())

# # isupper
# str26 = 'sadfsdfs'
# print(str26.isupper())

# str27 = 'EFKSDLJK'
# print(str27.isupper())

# str28 = '32424'
# print(str28.isupper())

# istitle
# str29 = 'Python Is Great'
# print(str29.istitle())

# str30 = 'I Am 29 Yesrs Old'
# print(str30.istitle())

###########################

#strip()

## only left and right sides spaces can be removed not between the words

# str31 = '            Hello Bujji    '
# print(str31)
# print(str31.strip())
# print(str31.lstrip())
# print(str31.rstrip())

#####################

# INDEXING

# str32 = 'Where what there is a will, there is way'
# print(str32.find('will'))
# print(str32.index('will'))
# print(str32.rfind('will'))
# print(str32.rindex('will'))

#######################

# SLICING

# str33 = 'MANORAMA'
# print(str33[0:3:1])
# print(str33[4:7:1])

# print(str33[-8:-4:1])
# print(str33[-4::1])
# print(str33[-8:-1:2])

# print(str33[6:2:-1])
# print(str33[-2:-6:-1])
# print(str33[7:0:-2])
# print(str33[-1:-8:-2])
