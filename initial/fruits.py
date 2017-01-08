# Fruits.py
# Python2
# Andresito de Guzman


import sys
import os
import math

##

# Clears the screen
def clearInterface():
    os.system('clear')

# Exits Program    
def exitProgram():
    clearInterface()
    print '''
    
    
    
    Thank you for using Hello Fruits!
    
    Press Enter to quit program
    
    
    
    
    
    
    '''
    quit()

# Return to Main Menu
def returnChoice():
    print "1 - Return to Main Menu"
    while True:
        try:
           choice = int(raw_input('What number? '))
        except ValueError:
            continue
        else:
            break
    if choice == 1:
       beginInterface()
    else:
        print "Not in the choices"
        returnChoice()

##
def aboutProgram():
    clearInterface()
    print '''
        ABOUT HELLO FRUITS!
    
    This program is created by Andresito de Guzman.
    
    Visit http://andre.is-great.net
    
    
    July 2016
    
    
    
    '''
    returnChoice()
##

fruits = {''}
        
def addFruit():
    clearInterface()
    print '''
        ADD FRUIT
        Enter the name of the fruit you would like to add. Type MENU to return to main menu.
    '''
    while True:
      try:
        add = raw_input('Fruit: ')
      except ValueError:
        print "Please type a fruit to continue or MENU to return"
        continue
      else:
        break
   
    if add == "MENU":
       returnChoice()
    elif add == "":
       print "You can't add an empty value"
       returnChoice()
    else:
      if add in fruits:
          print add + " is already in the list"
          print '''
          
          
          '''
          returnChoice()
      else:
          fruits.add(add)
          print add + " was add successfully!"
          print '''
          
          
          '''
          returnChoice() 

def listFruit():
    clearInterface()
    print '''
        LIST ALL FRUITS
        


    Here are the fruits:

    '''
    
    for fruit in fruits:    
        print  "* " + fruit
    print '''
   
   
    '''
    returnChoice() 

def removeFruit():
    clearInterface()
    print '''
        REMOVE FRUIT
        
    What fruit would you like to remove?
    (Case-sensitive)
    '''
    
    while True:
        try:
           remove = raw_input('Fruit: ')
        except ValueError:
           print "Place the name of the Fruit"
           continue
        else:
            break
    if remove in fruits:
        fruits.remove(remove)
        print remove + " was removed successfully"
        print '''
        
        
        '''
        returnChoice()
    else:
        print remove + " was not found"
        print '''
        
        
        '''
        returnChoice()

##
def MainMenuMessage():
    print "===== HELLO FRUITS! ====="
    print '''

    What do you want to do?
    
    1 - Add Fruit
    2 - Remove Fruit
    3 - List all Fruits
    
    4 - About Program
    5 - Exit Program
    

    '''
def MainMenuChoose():
    while True:
       try:
         choice = int(raw_input('What number? '))
       except ValueError:
         print "Please put a number"
         continue
       else:
         break
    if choice == 1:
        addFruit()
    elif choice == 2:
        removeFruit()
    elif choice == 3:
        listFruit()
    elif choice == 4:
        aboutProgram()
    elif choice == 5:
        exitProgram()
    else:
        print "Not in the choices"
        MainMenuChoose()

def beginInterface():
    fruits.remove('')
    clearInterface()
    MainMenuMessage()
    MainMenuChoose()

## Runtime
beginInterface()