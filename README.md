# python compare list of objects and dictionaries
similar programs that use both

## Dictionary:

```
# unpickle if the file exists
import pickle

try:
    oDictionaryFile = open("emails.bin", "rb")
    dictEmails = pickle.load(oDictionaryFile)
    oDictionaryFile.close()
except:
    dictEmails = {}

while True:

    print("Choices:")
    print(" 1 to add")
    print(" 2 to delete")
    print(" 3 to list")
    print(" 4 to quit")

    sChoice = input("What is your choice? ")
    if(sChoice == "1"):
        sName = input("name ")
        sEmail = input("email ")
        dictEmails[sName] = sEmail
        print(dictEmails)
    elif(sChoice == "2"):
        sName = input("name ")
        del dictEmails[sName]        
        print(dictEmails)
    elif(sChoice == "3"):
        for sName in dictEmails:
            print("Name is: " + sName + " Email is: "
                  + dictEmails[sName])
    else:
        break

oDictionaryFile = open("emails.bin", "wb")
pickle.dump(dictEmails, oDictionaryFile)
oDictionaryFile.close()


```

## Object:

```
import pickle

class Item:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    def __str__(self):
        return(self.__name + "," + self.__price)
    def getName(self):
        return(self.__name)


try:
    oItemFile = open("shoppingCart.bin", "rb")
    aShoppingCart = pickle.load(oItemFile)
    oItemFile.close()
except:
    aShoppingCart = []

while True:

    print("Choices:")
    print(" 1 to add")
    print(" 2 to delete")
    print(" 3 to list")
    print(" 4 to quit")
    sChoice = input("What is your choice? ")
    if sChoice == "1":
        sItemName = input("Enter the name of your item: ")
        sPrice = input("Enter the Price of your item: ")
        aShoppingCart.append(Item(sItemName, sPrice))
    elif sChoice == "2":
        sItemName = input("Enter the name of your item: ")
        for oItem in aShoppingCart:
            if(oItem.getName() == sItemName):
                aShoppingCart.remove(oItem)
                break
    elif sChoice == "3":
        for oItem in aShoppingCart:
            print(oItem)
    elif sChoice == "4":
        break
    

oItemFile = open("shoppingCart.bin", "wb")
pickle.dump(aShoppingCart, oItemFile)
oItemFile.close()

```