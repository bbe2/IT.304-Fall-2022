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
os.chdir('c:\\Users\\17574\\Desktop\\data') #microsoft uses 2 \\
df0 = pd.DataFrame() #explicitly set the data object
df0 = pd.read_excel("shakes_corpus_v1.xlsx") #ETL method 2
#df0.info()
mydict = df0.to_dict()
#===========================================================
#=>1.0 Pillar: Iterators
'''1.1 Task: use an iterator and produce total words all plays'''
#===========================================================

#==> ENTER YOUR CODE HERE
mylist = []


# Answer: 1,212,379

'''1.2 Task: what is easiest in code to double total characters'''
#==> ENTER YOUR CODE HERE


# Answer: 2424758

#===========================================================
#=> 2.0 Pillar: Functions
'''Task: Generate a tuple wth the code provided
   hint: use codebook if dont know function yet'''
#===========================================================
mylist = []
mytuple = ()
for i in range(37):
    mylist.append(i)
    
#==> ENTER YOUR CODE HERE


# Answer: 
print(mytuple)         # (0,1,..............36)
print(type(mytuple))   # <class 'tuple'>

#===========================================================
#=> 3.0 Pillar: Built-in objects - Sets
#===========================================================
''' 3.1 Quickly explain what this statement is doing
    
    random.randint(len(mydict),len(df0['script']))

    3.2 What does the type() function tell you and why is it
        important?
    3.3 Create one set from mydata1 and mydata2 and print it
    3.4 Use the type() function to prove new variable is a set
    3.4b How long is the new set and why
    3.5 Why is performing housekeeping a good habit?'''
#===========================================================

import random  # generates random numbers
               # randint(start value, end value)
mydata1 = random.randint(len(mydict),len(df0['script']))
print(len(mydict),len(df0['script'])) #4, 37

#==> 3.1 ENTER YOUR RESPONSE HERE


#==> 3.2 ENTER YOUR RESPONSE here after these 3 lines of code
print(type(mydata1))
mydata1 = (mydata1,)  #'''think! why is this needed'''
print(type(mydata1))  
   # 3.2 ENTER YOUR RESPONSE 

'''just think you will be a wizard once you master built in data objects'''


#==> 3.3 ENTER YOUR RESPONSE HERE
mydata2 = 1,2,3,4,3,2,1


#==> 3.4 ENTER YOUR RESPONSE HERE


#...ANSWERS:
#Answer: <your code answers should be the same except m
       #each person will have 1 diff value
print(mydata1,set(mydata2))     # (34,) {1, 2, 3, 4}
print(myset)                    # {1, 34, 3, 2, 4}
print(len(myset))   # 3.4b => 5
print(type(myset))  # <class 'set'>
#Answer built in objects only take one parameter. 
'''can only add objects that are the same object type'''


#==> 3.5 ENTER YOUR RESPONSE HERE - Housekeeping
del mydata1; del mydata2;del myset



#===========================================================
#= 4.0 Pillar - interpreting packed built-in objects
#===========================================================
'''Task: you have the following object visible to your in your
   'variable explorer' window. if script is in the ... describe
   the object container around it and what you would do to
    unpack it.'''
#===========================================================
'''             [({...})],   '''
#===========================================================