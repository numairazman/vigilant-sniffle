import os
#interacts with the file system
import fileinput

def menuDisplay():
# defining the function menuDisplay. all the code under def menuDisplay will be executed the next time
# menyDisplay is called upon
    print('=============================')
    print('= Inventory Management Menu =')
    print('=============================')
    #Header
    print('(1) Add New Item to Inventory')
    print('(2) Remove Item from Inventory')
    print('(3) Update Inventory')
    print('(4) Search Item in Inventory')
    print('(5) Print Inventory Report')
    print('(99) Quit')
    CHOICE = int(input("Enter choice: "))
    menuSelection(CHOICE)

def menuSelection(CHOICE):
    # defining the function menuSelection. all the code under def menuSelection will be executed the next time
    # menuSelection is called upon
    if CHOICE == 1:
        addInventory()
    # if the choice that the user enters is 1 then new item is added to inventory
    elif CHOICE == 2:
        removeInventory()
    # if the choice that the user enters is 2 then item is removed from inventory
    elif CHOICE == 3:
        updateInventory()
    # if the choice that the user enters is 3 then the inventory is updated
    elif CHOICE == 4:
        searchInventory()
    # if the choice that the user enters is 4 then they can search a new item
    elif CHOICE == 5:
        printInventory()
    # if the choice that the user enters is 5 then the inventory report is printed
    elif CHOICE == 99:
        exit()
    # if the choice that the user enters is 99 then they quit
    
def addInventory():
# defining the function addInventory. all the code under def addInventory will be executed the next time
# addInventory is called upon
    InventoryFile = open('Inventory.txt', 'a')
    #opens up the inventory file called inventory.txt and this is when a is selected by the user
    print("Adding Inventory")
    print("================")
    item_description = input("Enter the name of the item: ")
    #The item description input is where the item name is entered
    item_quantity = input("Enter the quantity of the item: ")
    #The item quantatity input is where the quantity of the item is entered
    InventoryFile.write(item_description + '\n')
    #The item description is added to the inventory file then a line is skipped in the output 
    InventoryFile.write(item_quantity + '\n')
    #The item quantity is added to the inventory file then a line is skipped in the output  
    InventoryFile.close()
    #The inventory file is closed
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    #The user is given the choice to either enter 98 to continue on and 99 to exit. 
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
    #If the user enters 98 then menuDisplay is called upon and all the options come up
    #If the user enters 99 then the program is exited
    
def removeInventory():
# defining the function removeInventory. all the code under def removeInventory will be executed the next time
# removeInventory is called upon
    print("Removing Inventory")
    print("==================")
    #Header is printed
    item_description = input("Enter the item name to remove from inventory: ")
    #User is asked to enter the item description 
    file = fileinput.input('Inventory.txt', inplace=True)
    #the user is asked to enter the file name???

    for line in file:
         if item_description in line:
             for i in range(1):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    item_description
    #dont understand the for loop
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
    #If the user enters 98 then menuDisplay is called upon and all the options come up
    #If the user enters 99 then the program is exited
    
def updateInventory():
# defining the function updateInventory. all the code under def updateInventory will be executed the next time
# updateInventory is called upon
    print("Updating Inventory")
    print("==================")
    #Header is printed 
    item_description = input('Enter the item to update: ')
    #asking user input to enter the name of the item that they wan to enter 
    item_quantity = int(input("Enter the updated quantity. Enter - for less: "))
    #asking user to enter the updated quantity and enter - to remove inventory?

    with open('Inventory.txt', 'r') as f:
        filedata = f.readlines()
    #while the inventory txt is opened, all the lines are read
    replace = ""
    line_number = 0
    count = 0
    #replace the file with quotations starting with line 0 
    f = open('Inventory.txt','r')
    #open the the inventory  file
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if item_description in line:
            for b in file[i+1:i+2]:
                value = int(b)
                change = value + (item_quantity)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1 
    #dont understant the for loop     
    f.close()
    #close the file
    
    filedata[count] = replace + '\n'

    with open('Inventory.txt', 'w') as f:
        for line in filedata:
            f.write(line)
                                            
                
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
    #If the user enters 98 then menuDisplay is called upon and all the options come up
    #If the user enters 99 then the program is exited
def searchInventory():
# defining the function searchInventory. all the code under def searchInventory will be executed the next time
# searchInventory is called upon
    print('Searching Inventory')
    print('===================')
    #Header for searching inventory
    item_description = input('Enter the name of the item: ')
    #Enter the name of the item that you want to search up
    f = open('Inventory.txt', 'r')
    #open the inventory text file
    search = f.readlines()
    f.close
    for i, line in enumerate(search):
        if item_description in line:
            for b in search[i:i+1]:
                print('Item:     ', b, end='')
            for c in search[i+1:i+2]:
                print('Quantity: ', c, end='')
                print('----------')
        
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
    #If the user enters 98 then menuDisplay is called upon and all the options come up
    #If the user enters 99 then the program is exited    
def printInventory():
# defining the function printInventory. all the code under def printInventory will be executed the next time
# printInventory is called upon
    InventoryFile = open('Inventory.txt', 'r')
    #open the inventory text file
    item_description = InventoryFile.readline()
    print('Current Inventory')
    print('-----------------')
    #header for current inventory 
    while item_description != '':
        #if the item description is not equal to ''
        item_quantity = InventoryFile.readline()
        #read the item quantity in the inventory file 
        item_description = item_description.rstrip('\n')
        #get rid of all the new lines in the description
        item_quantity = item_quantity.rstrip('\n')
        #get rid of all the new lines in the quantity
        print('Item:     ', item_description)
        print('Quantity: ', item_quantity)
        print('----------')
        #print the item and the quantity 
        item_description = InventoryFile.readline()
    InventoryFile.close()
    #close the inventory file

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
    #If the user enters 98 then menuDisplay is called upon and all the options come up
    #If the user enters 99 then the program is exited   
menuDisplay()
