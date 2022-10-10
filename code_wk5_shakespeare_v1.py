"""# -*- coding: utf-8 -*-
Created Sep 25 07:58:23 2022 @author: 17574 b.hogan@snhu.edu it.304.fall.22
"""

#ETL method 1, comma seperated. Pandas didn't like huge text
#raw_data = pd.read_csv("shakes_corpus_v1.csv") #did not like text data

#=======================================================================
#=>STEP 0 get pip library install path from https://pypi.org/
#=======================================================================
import pandas as pd              #dataframe library
import numpy as np               #numeric library
import matplotlib.pyplot as plt  #visualization library

#=======================================================================
#=>STEP 1: save files to data then set OS path to ETL it
# os = operating system, ETL = extract, translate, load
#=======================================================================
import os
os.getcwd()  #where am i, where do i need to be
#os.chdir('c:\\Users\BBE\DATA\') #some op.sys use one slash  
os.chdir('c:\\Users\\17574\\Desktop\\data') #microsoft uses two\\
os.getcwd()

df0 = pd.DataFrame()  #pandas dataframe are spreadsheet like but much more

#ETL method 2 -------> one is pd.read_csv('.csv')
df0 = pd.read_excel("shakes_corpus_v1.xlsx") #ETL method 2
df0.info()
   #             <class 'pandas.core.frame.DataFrame'>
   #             RangeIndex: 37 entries, 0 to 36
   #             Data columns (total 3 columns):
   #              #   Column  Non-Null Count  Dtype 
   #             ---  ------  --------------  ----- 
   #              0   name    37 non-null     object
   #              1   script  37 non-null     object

print(type(df0))  #pandas.core.frame.DataFrame
df0.head()
    #                                        name  ...    type
    #                0  Alls Well That Ends Well  ...  Comedy
    #                1            As You Like It  ...  Comedy

#=======================================================================
#=>STEP 2: Inspect data size, keys, and what would be best
#           to view and work with it
#=======================================================

#move data into the built-in objects your training in:
    # dict, list, etc
mydict = df0.to_dict()
print(mydict.keys())

mylist_keys = list(zip(mydict.keys())) 
mylist_keys    # [('title',), ('script',), ('type',), ('ID',)]

#now inspect the HUGE data
mylist_values = list(zip(mydict.values())) #holy cow this is huge!
mylist_values  #DANGER Will Robinson this is a megasaurus
 #  35: 'Tragedy',
 # 36: 'Tragedy'},),
 #{0: 1,
 #1: 2,
 # 2: 3,

#=======================================================================
#=>STEP 3:   Pillar EXERCISES
#=======================================================
#3.1 - Core Object Dictionary
#learn new dictionary function .get()
mydict.get('title')  #.get() views one series
play_names = [mydict.get('title')]
play_names
        [{0: 'Alls Well That Ends Well',
          1: 'As You Like It',
          2: 'The Comedy of Errors',
# Now add titles to a different object with an iterator
mylist = []
for i in [mydict.get('title')]:
    mylist.append(i)
mylist
    [{0: 'Alls Well That Ends Well',
      1: 'As You Like It',
      2: 'The Comedy of Errors',
#3.2 =>  Learn dictionary key, value, items parameters
mylist_key =  []
mylist_values = []
for k,v in mydict.items():
    mylist_key.append(k)
    mylist_values.append(v)
    print(v)
mylist_key
#3.3 =>  Understand and count items in a list
len(mylist_values) #hmm  why is this only four ?
mylist_values[0]
mylist_values[1]
mylist_values[2]
mylist_values[3]

#3.4 =>  Functions - now get some meta data
https://docs.python.org/3/library/functions.html#built-in-functions

sum(mylist_values[3])-1  #665 #yikes dont want a bad number!

#3.5 => do the same with an iterator and a variable
x = 0
for i in mylist_values[3]:
    x = x + int(i)   #specific if want number, str, etc
print(x-1)  #665
    
#3.6 now lets count characters
my_sub_list = [mylist_values[0]]
my_sub_list[0]          #list
type(my_sub_list[0])    #dict

#=========================
#print("{a}".format(a=1.01))































