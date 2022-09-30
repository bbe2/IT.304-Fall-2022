"""# -*- coding: utf-8 -*-
Created Sep 25 07:58:23 2022 @author: 17574 b.hogan@snhu.edu it.304.fall.22
"""
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
#ETL method 1, comma seperated. Pandas didn't like huge text
#raw_data = pd.read_csv("shakes_corpus_v1.csv") #did not like text data

#ETL method 2
df0 = pd.read_excel("shakes_corpus_v1.xlsx") #ETL method 2
df0.info()
   #             <class 'pandas.core.frame.DataFrame'>
   #             RangeIndex: 37 entries, 0 to 36
   #             Data columns (total 3 columns):
   #              #   Column  Non-Null Count  Dtype 
   #             ---  ------  --------------  ----- 
   #              0   name    37 non-null     object
   #              1   script  37 non-null     object
   #              2   type    37 non-null     object

print(type(df0))  #pandas.core.frame.DataFrame
df0.head()
    #                                        name  ...    type
    #                0  Alls Well That Ends Well  ...  Comedy
    #                1            As You Like It  ...  Comedy
    #                2      The Comedy of Errors  ...  Comedy
    #                3                 Cymbeline  ...  Comedy
    #                4        Loves Labours Lost  ...  Comedy

#move data into the built-in objects your training in: dict, list, etc
mydict = df0.to_dict()
print(mydict.keys())

mylist_keys = list(zip(mydict.keys())) #hmm my data columns looks good
mylist_keys

#now inspect the HUGE data
mylist_values = list(zip(mydict.values())) #holy cow this is huge!
mylist_values  #DANGER Will Robinson this is a megasaurus

#finally break data into more manageable things to do
mydict.get('title')  #learn a new function
play_names = [mydict.get('title')]
play_names

for i in play_names:
    print(i)

mylist = [(key, value) for key, value in mydict.items]





































