"""# -*- coding: utf-8 -*-Created on Mon Oct 12 10:59:53 2022
@author:17574 b.hogan@snhu.edu it.304.fall.22
# WEEK 7 CODE final - including classes """

                        #=========================================
                        #=>week 7  Object Classes Overview
                                #===================================
        
Lexical Analysis
        always remember about indent \ dedent!
        if you copy and paste and teh spacing is wrong it wont run

https://python.readthedocs.io/en/latest/reference/lexical_analysis.html
        

#Create a report structure                                
mydict = {"training done":[], "total animals":0} 
class myFarm:    #create parent class object 
    pass           
    name = ""
    species = ""
    train = ""
def add_train(traintype):    #create a user function to count, sort
    mydict["training done"].append(traintype)
    mydict["total animals"] =+1

#------------->   #children instantiate from parents
a1 = myFarm()     # instantiate children objects from parent, a for animal 
a2 = myFarm()     # all object names are user defined

#update attributes
a1.name = 'mackenzie'  #object.attribute or object.function
a1.species ='dog'
a1.train = 'speak'
add_train(a1.train) #cheCK-OUT! 	<only here bc space>

a2.name = 'vinny'
a2.species = 'horse'
a2.train = 'jumping'

add_train(a2.train) #'''function accepts attribute to update dictionary object'''

#write a simple report using a dictionary data object format
mydict_rpt = {a1.name:a1.species, a2.name:a2.species,"metrics=>":mydict}
mydict_rpt
 '''{'arnold': 'dog','vinny': 'horse','metrics=>': 
     {'training done': ['catch', 'jumping'], 'total animals': 1}}'''

#use object’s constructors to view its contents
print(a1.__dict__,a2.__dict__)
   ''' {'name': 'arnold', 'species': 'dog', 'train': 'catch'}
     {'name': 'vinny', 'species': 'horse', 'train': 'jumping'}'''

help(a1)
dir(a1)
['__class__', '__delattr__', '__dict__','__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
 '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__','__setattr__', '__sizeof__','__str__', '__subclasshook__',
 '__weakref__',
 'name',
 'species',
 'train']

                                '''#====================
        #============================================================
                        #=>Week 7 Objects part II
        #============================================================
                                    #========================'''


class dog_train:
    name = ""
    num_fetch_train = 30
    num_fetched = num_fetch_train
    trainer_ok = 0
    
    def fetch_train(self, num_balls):
        self.num_fetched = self.num_fetched - num_balls
        if self.trainer_ok == 0 and self.num_fetched <= 0:
            return "sorry! {} not fetch trained. {} balls over a target of {}".format(self.name,abs(self.num_fetched),self.num_fetch_train)
        elif self.trainer_ok == 1:
            return "Whew! {} passes training after {} balls".format(self.name, abs(self.num_fetch_train-self.num_fetched-1))
        else:
            return"{} on target to pass fetch train with {} balls left".format(self.name,self.num_fetch_train-self.num_fetched)

dog1 = dog_train()
dog1.name = "cheeseman"
print(dog1.fetch_train(9))
print(dog1.fetch_train(31))
dog1.trainer_ok = 1
print(dog1.fetch_train(1))


                                '''#====================
        #============================================================
                        #=>Week 7 Graded QU/iz Assignment
        #============================================================
                                    #========================'''

====================
#==========================
#============================================================
#=> it.304 2nd Graded Assignment - ANSWERS
#============================================================
#========================"""
import pandas as pd              #dataframe library
import numpy as np               #numeric library
import matplotlib.pyplot as plt  #visualization library
import os
os.chdir('c:\\Users\\17574\\Desktop\\data_it304') #microsoft uses 2 \\
df0 = pd.DataFrame() #explicitly set the data object
df0 = pd.read_excel("data_shakes_corpus_v1.xlsx") #ETL method 2
df0.info()
mydict = df0.to_dict()  #dataframe to python dictionary !
''''mydict = megadict = {'title':{},'script':{},'type':{},'ID:{} }'''
mydict

'''
#37 rows x 4 xcolumns
         col-0  |  col-1  | col-2  | col-3
header   title  |  script | type   | id
row-0 = 1st line; total = 37 rows or 37x4 (R x C)'''

#===================================
#=>1.0 Pillar: Iterators
'''1.1 Task: use an iterator and produce total words all plays'''
#===================================

#==> ENTER YOUR CODE HERE
mylist = []
for i in mydict['script'].values():
    mylist.append(i)
total_script_characters= 0    #how many characters?
for i in mylist:
    total_script_characters = total_script_characters + len(i)
total_script_characters

# Answer: 1,212,379

'''1.2 Task: what is easiest in code to double total characters'''
#==> ENTER YOUR CODE HERE
https://docs.python.org/3/library/stdtypes.html#built-in-types

total_script_characters*2   '''use regular math operators"

# Answer: 2424758

#===================================
#=> 2.0 Pillar: Functions
'''Task: Generate a tuple wth the code provided
   hint: use codebook '''
#===================================
mylist = []
mytuple = ()
for i in range(37):
    mylist.append(i)
    
#==> ENTER YOUR CODE HERE
mytuple = tuple(mylist)  #USE core python functions list(), dict()
                        '''list(), dict(), tuple(), set(), "str"'''

# Answer: 
print(mytuple)         # (0,1,..............36)
print(type(mytuple))   # tuple

#======================================
#=> 3.0 Pillar: Built-in objects - Sets
#=======================================
"""3.1 Quickly explain what this statement is doing
    
    random.randint(len(mydict),len(df0['script']))

    3.2 What does the type() function tell you and why is it
        important?
    3.3 Create one set from =mydata1 and mydata2 
    3.2 Use the type() function to prove it is a set
    3.5 Why is performing housekeeping a good habit?"""
#===================================
import random  # generates random numbers'''
               # randint(start value, end value)
mydata1 = random.randint(len(mydict),len(df0['script']))
print(len(mydict),len(df0['script'])) #4, 37

#==> 3.1 ENTER YOUR RESPONSE HERE


#==> 3.2 ENTER YOUR RESPONSE here after the 3 lines of code
print(type(mydata1))
mydata1 = (mydata1,)
print(type(mydata1)) '''can only add objects that are the same object type'''

#==> 3.2 ENTER YOUR RESPONSE HERE
mydata2 = 1,2,3,4,3,2,1
myset = set(mydata1 + mydata2)

#...ANSWERS:
#Answer: <your code answers should be the same except m
       #each person will have 1 diff value
print(mydata1,set(mydata2))     # 35, {1,2,3,4}
print(myset)                    # {1, 2, 3, 35, 4}
print(len(myset))   # 3.1 => 4
print(type(myset))  # <class 'set'>

#Answer help, built in objects only take one parameter. 
# BUT you can add objects together as long as they are the same
# object type.


# housekeeping
#Why: so dont absob data you dont need later by accident
del mydata1; del mydata2;del myset

#===================================
#= 4.0 Pillar - interpreting packed built-in objects
'''Task: you have the following object visible to your in your
   'variable explorer' window. if script is in the ... describe
   the object container around it and what you would do to
    unpack it.'''
#===================================
'''             [({...})],   '''
#===================================
the string data is in a dictionary {key:valuye}
        which is inside a tuple
            which is inside a list

====================
#==========================
#============================================================
'''end graded assignment 1 of 2 for week 2'''
#============================================================
#========================"""


#==> Moved to assignment 2 - for Week 8
#===================================
#=>STEP 5.3.4: Challenge - 
#       a) create a tuple using a plays numeric ID
#       b) have titles in a list
#       c) have scripts in a list
#       d) use a while iterator to loop through both lists
#         d1) have tuple point to title or script
#         d2) count total characters in both
#         d3) create anytype of report to display
#===================================
























                                    #==========================
#============================================================
                                    #=>WEEK6 FOUNDATION CODE
#============================================================
                                    #=========================="""


#==========================
#============================================================
#=>STEP I - GET DATA
#============================================================
#=========================="""
import pandas as pd              #dataframe library
import numpy as np               #numeric library
import matplotlib.pyplot as plt  #visualization library
import os
os.getcwd()            #where am i? <get working directory>
#os.chdir('c:\\Users\BBE\DATA\') #some op.sys use one slash  
os.chdir('c:\\Users\\17574\\Desktop\\data_it304') #microsoft uses 2 \\
os.getcwd()

df0 = pd.DataFrame() #explicitly set the data object
#df0 = pd.read_csv("data_shakes_corpus_v1.csv")   #ETL method 1
df0 = pd.read_excel("data_shakes_corpus_v1.xlsx") #ETL method 2
df0.info()
   #             RangeIndex: 37 entries, 0 to 36
   #             Data columns (total 3 columns):
   #              #   Column  Non-Null Count  Dtype 
   #             ---  ------  --------------  ----- 
   #              0   title   37 non-null     object
   #              1   script  37 non-null     object
   #              2   type    37 non-null     object
   #              3   ID      37 non-null     int64 
   #             dtypes: int64(1), object(3) memory usage: 1.3+ KB

print(type(df0))  #use type() to always see what an object is
df0.head()
    #                                   title  ...    type
    #             0  Alls Well That Ends Well  ...  Comedy

#2.1 use pandas df.to_dict() to move data into dictionary object
mydict = df0.to_dict()
print(mydict.keys())    #['title', 'script', 'type', 'ID'])
type(mydict.keys())     # object itself is keys

#2.2 understand what a dictionary and zip is doing
mylist_keys = list(zip(mydict.keys())) 
mylist_keys    # [('title',), ('script',), ('type',), ('ID',)]

#Inspect huge data and then break into smaller chunks
mylist_values = list(zip(mydict.values())) #WOW huge !
#point - zip helpful but continue to learn more functions

mylist_values   #=======================> #MEGASAURUS 
                     #  35: 'Tragedy',
                     # 36: 'Tragedy'},), #this comma is a new object
                     #{0: 1,
                     # 1: 2,
'''=====================
#==========================
#============================================================
#=>STEP 2 - seperate Megasaurus into usuable object chunks
#============================================================
#==========================
#====================='''

'''2.1'''
type(mylist_values) #=> [({...})], 

'''======> packed as [({...})], =>list, tuple, dictionary'''

type(type(mylist_values[1]) )#hmm doesn't unpack
len(mylist_values)  #=> 4 columns in spreadsheet, ie data objects

                    '''megasaurus - all plays and words'''
mylist_values
                        # => format is list[(tuple(dict))]
                        # [  ({id:title}),({id:script}),
                        #    ({id:type}), ({id:id}) ]
                        # zip added an key sequential value
'''==>2.2'''          
'''use slicing [0:1], [2] to view next level down'''
type(mylist_values[0])  # tuple                   
mylist_values[0]        #=> [x] is called slicing      
           
           #       Out[23]: 
           #       ({ 0: 'Alls Well That Ends Well',
           #          1: 'As You Like It',             

'''now think data like in spreadsheet'''
#  columns
#    0      1     2      3
# |title |script| type |  id  |
#  hamlet,oh joy,tragedy, 29

mylist_values[1] #displays all the script text! 

'''==>2.3''' 
len(mylist_values[1])  # waits its '1' so need to unpack my data

mylist = []
for i in mydict['title'].values():
    mylist.append(i)
mylist
len(mylist)  #37 - does htat match spreadsheet? always know your bounds

title_total_characters = 0    #how many characters?
for i in mylist:
    title_total_characters = title_total_characters + len(i)
title_total_characters  #do you get 560 ?

#==========================
#============================================================
#=>STOP! : view 'Variable Explorer' window
#  use this feature to propel data transformation learning
#============================================================
#==========================


'''==>2.5''' 
'''#=====================
#=> WRAP - UP  Housekeeping
#  delete variables not using; help avoid unnecssary mistakes'''
del mylist_values
del mylist_keys
#==========
# be mindful how you stage both variable and data names
#   df0 = baseline import
#       df1 = analysis 1
#           df2 = analysis 2
#==================='''

'''  this is an example having data go to a wrong variable bc not deleted
mylist2 = []
for i in [mydict.get('title')]:
    mylist.append(i)   #so what happended here a. wrote name list wrong
print(len(mylist2), len(mylist))
#make a note here on what happended...............
mylist    #stacked a list on a dictionary bc meant to use list2
'''
#go back and rest data for part 2
mylist = []
for i in mydict['title'].values():
    mylist.append(i)

#==========================
#============================================================
#=>STEP 3:  Use dir(object) to learn its methods to get work done
#============================================================
#==========================
'''==>3.1'''
#===============> use dir() to get functions available for an object
myset = set()
print(type(myset))
dir(myset)
 # '__xor__',  ==> these are constructors, more later
 #    'add', 'clear',    ==> these are methods
 #   'copy','difference', 'difference_update', 'discard',
 #  'intersection','intersection_update', 'isdisjoint', 'issubset',
 #   'issuperset','pop', 'remove','symmetric_difference',
 #   'symmetric_difference_update','union',  'update']'''

'''==>3.1'''# ====> SETS
mylist2 = mylist
mylist2.append("Winters Tale")  #add one duplicate title
myset = set(mylist2)
print(len(mylist),len(myset))  #so got rid of duplicate
del mylist2

#============> ACTION learn what you need and go find it
mystring = ""
print(type(mystring))
dir(mystring)
#'''__subclasshook__',  'capitalize', 'casefold',, 'center',
#'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
#'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
#'isdigit', isidentifier', 'islower', 'isnumeric', 'isprintable',
#'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
#'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
#'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines','startswith', 
#'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']'''

#==========================
#============================================================
#=>STEP 4: More dictionary: .keys(), .values(), .get(<key>)
#============================================================
#==========================

'''==>4.1'''
mydict.get('title')  #.get() views one series
play_names = [mydict.get('title')]
play_names
        [{0: 'Alls Well That Ends Well',
          1: 'As You Like It',
          2: 'The Comedy of Errors',
mylist
# Now add titles to a different object with an iterator
mylist2 = []
for i in [mydict.get('title')]: #method returns a dict obj
    mylist2.append(i)
mylist2
    [{0: 'Alls Well That Ends Well',
      1: 'As You Like It',
      2: 'The Comedy of Errors',
      
#3.2 =>  Learn dictionary key, value, items parameters
mylist_key =  []
mylist_values = []
for k,v in mydict.items():
    mylist_key.append(k)
    mylist_values.append(v) 
mylist_key              #['title', 'script', 'type', 'ID']
mylist_values   #'''again megasaurus'''

'''==>4.2''' #=>  Understand and count items in a list
len(mylist_values) #hmm  why is this only four ?
mylist_values[0]
mylist_values[1]
mylist_values[2]
mylist_values[3]

#==========================
#============================================================
#=>STEP 3:  Use Functions and get Meta Data
#============================================================
#==========================

https://docs.python.org/3/library/functions.html#built-in-functions

sum(mylist_values[3])-1
sum(df0['ID'])-1
len(set(df0['ID']))

#==============> we will do more of this together

END END END END END END END END END WEEK-6 WEEK-6 WEEK-6
