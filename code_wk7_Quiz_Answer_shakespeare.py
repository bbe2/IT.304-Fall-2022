"""# -*- coding: utf-8 -*-
Created on Mon Oct 10 10:59:53 2022
@author: 17574
====================
#==========================
#============================================================
#=> it.304 2nd Graded Assignment
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
mydict = df0.to_dict()
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

total_script_characters*2

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
mytuple = tuple(mylist)

# Answer: 
print(mytuple)         # (0,1,..............36)
print(type(mytuple))   # tuple

#======================================
#=> 3.0 Pillar: Built-in objects - Sets
#=======================================
''' 3.1 Quickly explain what this statement is doing
    
    random.randint(len(mydict),len(df0['script']))

    3.2 What does the type() function tell you and why is it
        important?

    3.3 Create one set from =mydata1 and mydata2 
    3.2 Use the type() function to prove it is a set
    3.5 Why is performing housekeeping a good habit?'''
#===================================

import random  # generates random numbers
               # randint(start value, end value)
mydata1 = random.randint(len(mydict),len(df0['script']))
print(len(mydict),len(df0['script'])) #4, 37

#==> 3.1 ENTER YOUR RESPONSE HERE


#==> 3.2 ENTER YOUR RESPONSE here after the 3 lines of code
print(type(mydata1))
mydata1 = (mydata1,)
print(type(mydata1))

'''can only add objects that are the same object type'''

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
the string data is in a dictionary
which is inside a tuple
which is inside a list

====================
#==========================
#============================================================
'''end graded assignment 1 of 2 for week 2'''
#============================================================
#========================"""


#==> Moved to assignment 2
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










