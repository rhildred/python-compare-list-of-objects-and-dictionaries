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
