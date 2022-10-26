"""  it.304 week 9 EXAM - 7 pillars of python
Created on Sat Oct 22 07:42:57 2022
@author: 17574 => b.hogan@snhu.edu """

#=> 7 Pillars of Python Exam - it.304 System Analysis and Design
#=> due date = none
#=> Please take your time. Good writing is good thinking
#=> Objectives & Overview: Show me your skills and creativity!
"""
Over the past few weeks have you have taken the time to learn Python data
structures, data pack/unpack, data transformation, conditionals, iterators, 
functions, and building your own object classes. Whew!

This is a significant undertakening and all autobots.it304 have performed
amazingly well. You have shown your capacity to think different and
"stick-to-it-ness." You are doing the work some others have trouble with.

It's a BIG DEAL you learned to play with all of Shakespeare's words! Now you 
are prepared to work with any book. And, you don't have to go scan it in.

For this exam you will work with 5 new books, transpose their data, count
things, and make reports. You will also ask a user what book they want to
read and send me the file. Excited? I hope so!

Books have project plans like the system project plans,Except the characters
generate the transactions by falling in love and blowing things up. Strangely,
you can use random number generators to build a matrix of character activities, 
places and things, print a script outline and send out for writer development.

You're now a jr. system designer, analyst, and information organizer. Keep
building your skills and you can be creative how organization is assembled.
~brian
"""
#=> c) EXAM SETUP
Install a library: Spyder docs say using conda better for them
terminal >>> cd \
         >>> cd "C:\Users\17574\anaconda3\"  #update for your user...
         >>> conda install -c anaconda nltk


#=> d) EXAM SETUP final test
import nltk   #natural language toolkit; 
              #more instructions if stuck: https://www.nltk.org/book/ch02.html
mylist = nltk.corpus.gutenberg.fileids()  # titles ONLY packed as a list
print(mylist)       

#---------------------------------------------------------------------------
#=> EXAM Part I    - replicate shakesprease spreadsheet from wks 5-8
#=>                - please answer the questions. you can rename as needed
#---------------------------------------------------------------------------
  #    Situation: unfortunately your business customer cant read the data b/c
  #    they can't open a text file in Microsoft word. PLEASE help them out.
  #      1a) get title: mytitles = nltk.corpus.gutenberg.fileids()
  #      1b) make sure the wrath of kahn equals the baseline Moby-dick import
  #      1c) get script data into python objects however you like
  #      1d) figure out how to delete or parse what you dont need using
  #          functions like mylist.pop[slice], .remove() or build new objects
  #      1f) create numeric indexID(equals old ID column): list(range(999))
  #      1g) create a dictionary, move to df, print(df), email me xls or txt

#---------------------------------------------------------------------------
#=> EXAM Part II   - calculate text and create a report
#=>                - please answer the questions. you can rename as needed
#---------------------------------------------------------------------------
#       2a) total words in title + total words in book for all 5 books
#           title | script  | number_sentences  | number_characters

#       2b) use iterators to count the words
#       2c) extra points if you can figure out how to use an iterator
#           to count words for titles scripts in on iterator
#       2d) packup to a dictionary to a df and export to a spreadsheet

#---------------------------------------------------------------------------
#=> EXAM Part III  - ask user what play they want to read and email the data
#=>                - please answer the questions. you can rename as needed
#---------------------------------------------------------------------------
#       3a) Create an object with one or two functions to ask user what
#           book they want to read, what format xls or txt
#       3b) Use objects created in part II to get data
#           hint: can either ask user to enter a number or enter title
#           response and equate it to a dictionary key... <end of hint>
#       3c) Optional: figure out something using conditional statements and
#           give the user additional informatoin



#       3d) Optional: provide user a wordcloud of what they will read


#=> a) EXAM SETUP
#=> installing new libraries is 


#fill in the blanks (please) - you might need it later >:0)
#    urObj_Name  | charcter code  |   explicit code 
#  i) mytuple =    (, )          => mytuple = tuple(myMindObject)
# ii) mylist = 
#iii) mydict = 
# iv) myset  = 
#v)dataframe =
#vi) mystring=



#=> b) EXAM SETUP 
''' *must have all 5 please*
Exam corpus:
 -- alice_in_wonderland
 -- moby_dick
 -- shakespeare_caesar  #and a few shakespeare since your familiar with him
 -- shakespeare_hamlet
 -- shakespeare_macbeth
'''

#=> c) EXAM SETUP
#Install a library: Spyder docs say using conda better for them
#terminal >>> cd \
#         >>> cd "C:\Users\17574\anaconda3\"  #update for your user...
#         >>> conda install -c anaconda nltk


#=> d) EXAM SETUP final test
import nltk   #natural language toolkit; 
              #more instructions if stuck: https://www.nltk.org/book/ch02.html
mylist = nltk.corpus.gutenberg.fileids()  # titles ONLY packed as a list
print(mylist)                             
    #['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 
    #   'bible-kjv.txt', 'blake-poems.txt','bryant-stories.txt', 
    # 'burgess-busterbrown.txt','carroll-alice.txt', 'chesterton-ball.txt', 
    #'chesterton-brown.txt','chesterton-thursday.txt','edgeworth-parents.txt', 
    #'melville-moby_dick.txt','milton-paradise.txt','shakespeare-caesar.txt', 
    #'shakespeare-hamlet.txt','shakespeare-macbeth.txt','whitman-leaves.txt']
    
#=========================================================                     
#=> STOP - if you see books above your good to go else email me. Congrats!
#=========================================================



#=> EXAM Part I    - replicate shakesprease spreadsheet from wks 5-8
#=> EXAM Part II   - calculate text and create a report
#=> EXAM Part III  - ask user what play they want to read and email the data


#---------------------------------------------------------------------------
#=> EXAM Part I    - replicate shakesprease spreadsheet from wks 5-8
#=>                - please answer the questions. you can rename as needed
#---------------------------------------------------------------------------

 # 1)  Replicate existing Shakespeare input spreadsheet with the 5 new books.
  #    Situation: unfortunately your business customer cant read the data b/c
  #    they can't open a text file in Microsoft word. PLEASE help them out.
  #      1a) get title: mytitles = nltk.corpus.gutenberg.fileids()
  #      1b) make sure the wrath of kahn equals the baseline Moby-dick import
  #      1c) get script data into python objects however you like
  #      1d) figure out how to delete or parse what you dont need using
  #          functions like mylist.pop[slice], .remove() or build new objects
  #      1f) create numeric indexID(equals old ID column): list(range(999))
  #      1g) create a dictionary, move to df, print(df), email me xls or txt

dir(nltk.corpus.gutenberg)  # QUESTION: what does dir() function tell you?
                            # urANSWER:
                            # [bonus: what is a __class__ or __dict__ called? 
                            # [urANSWER: starts w 'c'                 ]
                            #
                            
                            # QUESTION: how do you use dir() info smartly to
                            # get what you need done more quickly?
                            # urANSWER:
                            #
                            #
                            #
                            
                            # QEUSTION: based on dir(nltk.corpus.gutenberg) 
                            # what are THE best three attributes to run a 
                            # google query on to get this assignment done?
                            # also answer what you query in google
                            # urANSWER:
                            #
                            #
                            #
#-------------
#1a -title
#-------------
mylist_titles = nltk.corpus.gutenberg.fileids()
print(mylist_titles)        # QUESTION: how many books in the default library?
                            # urANSWER:
                            #
#---------------------------------------
#1b - wrath of kahn  - data double check
#---------------------------------------
data = nltk.corpus.gutenberg.sents('melville-moby_dick.txt')
print(type(data),len(data),data[0])
                            # QUESTION: what object type is the data in ?
                            # urANSWER:
                            #
                                
                            # QUESTION: what does 10059 mean?
                            # urANSWER:
                            #
                                
print(data[0])              # QUESTION: explain how the raw data is packed
                            # urANSWER:  
                            #
                            
mylist = list(nltk.corpus.gutenberg.sents('melville-moby_dick.txt'))
print(type(data))
print(type(mylist))
print(len(data))
print(len(mylist))
print(data[0])
print(mylist[0])            # QUESTION: what did mylist() function do?
                            # urANSWER: 
                            #       
                            # QUESTION: why even bother using list() ?
                            #---------------
                            # learningANSWER
                            #---------------
                            #           -> by converting to a python object
                            # you know, you also know how it will behave
                            # when transposing data between lists, tuples,
                            # dict, sets, and dataframes to suit your needs.
                            
                            # It is not wrong to use the nltk packed data type. 
                            # However it might not do what you expect!
                            # In the future query/read how a new object works.
            # query = nltk docs corpus.reader.util.StreamBackedCorpusView 
            # >>> image that, what is #1 in the list...
            # https://www.nltk.org/_modules/nltk/corpus/reader/util.html
                    
            # This is standard for data transformation
            # https://en.wikipedia.org/wiki/Data_transformation_(computing)

                            # Train on new objects you will use regularly
                            # to expand your Python data object mix/match
                            # knowledge.
                            # Many texts, etc dont explain or teach this.
                            # Welcome to the compute club autobots.it304
#----------------------------------------------------------------------------
print(len(mylist))          # QUESTION: what is 10059 mean?   
                            # urANSWER: 
print(mylist[0:4])       # start of book
print(mylist[10058:])    # end of book
                            # QUESTION: explain how data is packed
                            # urANSWER:
                            #
for i in data[0]:            
    print(i)                # QUESTION: explain what each iterator did    
for i in mylist[0]:         # urANSWER: 
    print(i)                #
                            # QUESTION: why is the data the same
                            #---------------
                            # learningANSWER
                            #---------------
                            # In this case the information is the same but
                            # that still doesn't mean for other transformations
                            # it would do what you want. Good to investigate!
                            
# nltk data provides data pack/unpack by variables raw, words, and sents
data = nltk.corpus.gutenberg.raw('melville-moby_dick.txt') 
print(data[0:30])
data = nltk.corpus.gutenberg.words('melville-moby_dick.txt') 
print(data[0:3])
data = nltk.corpus.gutenberg.sents('melville-moby_dick.txt')
print(data[0:3])
                            # QUESTION: explain how each variable is different 
                            # in terms of data pack and unpack. Also, what
                            # data pack do you think you would intially use
                            # knowing you need to send the client a text file
                            # of the book to read?
                            # urANSWER: 
                            #
                            #
                            #
              
print(data[10031])# wrath of Kahn script quote of moby-dic from star-trek movie

wrath_of_kahn = ""
for i in mylist[10031]:
  wrath_of_kahn = wrath_of_kahn + " " + i
print(wrath_of_kahn)
''' baseline kahn...
 Towards thee I roll , thou all - destroying but unconquering whale ; 
 to the last I grapple with thee ; from hell ' s heart I stab at thee ; 
 for hate ' s sake I spit my last breath at thee .
'''                         # QUESTION: explain what the iterator did
                            # urANSWER:
                                
           
            
           
            
#      1c) get script data (later you NEED to FIGURE Out how to UNPACK)
#      1d) get the rest of the book script data
#      1e) figure out how to delete or parse what you dont need using
#          functions like mylist.pop[slice], .remove() or build new objects
 #      1f) create numeric indexID(equals old ID column): list(range(999))
 #      1g) create a dictionary, move to df, print(df), email me xls or txt
                                
                                

#1c - get script data - figure out your unpack strategy
                    #=> has weird characters you dont want for this




  

#---------------------------------------------------------------------------
#=> EXAM Part II   - calculate text and create a report
#=>                - please answer the questions. you can rename as needed
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
#=> EXAM Part III  - ask user what play they want to read and email the data
#=>                - please answer the questions. you can rename as needed
#---------------------------------------------------------------------------



  # 2) Create a Report
#       2a) total words in title + total words in book for all 5 books
#           title | script  | number_sentences  | number_characters
words_play

#       2b) use iterators to count the words
#       2c) extra points if you can figure out how to use an iterator
#           to count words for either all titles, scripts, or both together
#           at the same time. 
#       2d) pack up the objects into a dictionary to df to spreadsheet

  #3) Create a Object Class asking a user what book of the 5 they want to read
#       3a) you can use the objects already up to top for this so no need
#           to rebuild them!
#       3b) You can do this any you want but one option is to take the user
#           response and equate it to a dictionary key... <end of hint>
#       3c) Optional: figure out something using conditional statements and
#           give the user additional informatoin
#       3d) Optional: hook up this wordcloud code to generate a graph of all
#           the most common words for the user in the book they will read






# 1) Read and write external xlsx, csv, or text data
#Situation
# your business client wasn't able to merge the data because there machine
# doesn't have enough memory. They have plays but can add the play types
# and they need a report of total chracters by play type (comedy,tragedy, etc)
# Task
# so cant add anything else to the script file
# import and combine the data into one dictionary and send back out so you 
# can email and show them how easy that was.

import pandas as pd                               #dataframe library
import numpy as np                                #numeric library
import matplotlib.pyplot as plt                   #visualization library
import os                                         #operating system library
import sys                                        # sys.exit()
os.chdir('c:\\Users\\17574\\Desktop\\data_it304') #microsoft uses 2\\
df0 = pd.DataFrame()                              #explicitly set datafarme
df0 = pd.read_excel("data_shakes_corpus_v1.xlsx") #ETL method 2
df0.info()# RangeIndex: 37 entries,0 to 36, 4 col=> all data u need to index
mydict = df0.to_dict()                            #df to dict
'''mydict_shakespeare => {'title':{},'script':{},'type':{},'ID:{} }'''
len(df0) #37    
  

df0


#report format goal
'''                         play1 | play2 | play...n
        characters title
        characters script                               '''



iterators 




class myobject:
    #attributes and data objects
    
    
    #function 1
    def myfunction1:
        return
    
    #function 2
    def myfunction2:
        return