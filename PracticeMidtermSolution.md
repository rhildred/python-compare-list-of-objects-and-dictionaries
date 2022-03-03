## (Partial) Solutions for Practice Midterm

1. Canadian Federal tax is calculated using the following formula: 

```

#calculate federal tax

#prompt for taxable income

nTaxable = int(input("Please enter your taxable income"))

#calculation
if nTaxable <= 45282:
    nPrevious = 0
    nMarginal = .15Final
    nPreviousTax = 0
elif nTaxable <= 90563:
    nPrevious = 45282
    nMarginal = .205
    nPreviousTax = 6792
elif nTaxable <= 140388:
    nPrevious = 90563
    nMarginal = .26
    nPreviousTax = 16075
elif nTaxable <= 200000:    
    nPrevious = 140388
    nMarginal = .29
    nPreviousTax = 29029
else:
    nPrevious = 200000
    nMarginal = .33
    nPreviousTax = 46317

#output
print("tax on", nTaxable, "=", (nTaxable - nPrevious) * nMarginal + nPreviousTax)


```

2. Volume

```
import math
#calculate volume

# input

nRadius = int(input("radius >"))

nHeight = int(input("height >"))

#output
print("the volume is", math.pi * nRadius **2 * nHeight, "cubic meters")

```

3. Vowels and consonants

```
sVowels = "aeiou"

def num_Vowels(sInput):
    nVowels = 0
    for ch in sInput:
        if ch in sVowels:
            nVowels += 1
    return nVowels

def num_Consonants(sInput):
    nConsonants = 0
    for ch in sInput:
        if ch not in sVowels and ch not in " .,!>?":
            nConsonants += 1
    return nConsonants

sUserInput = input("enter a string >")

print("the string contains", num_Vowels(sUserInput), "Vowels")

print("the string contains", num_Consonants(sUserInput), "Consonants")

```

4. Product Name and Price

```

dictPrices = {}

while True:

    print("Choices:")
    print(" 1 to add")
    print(" 2 to delete")
    print(" 3 to list")
    print(" 4 to quit")

    sChoice = input("What is your choice? ")
    if(sChoice == "1"):
        sName = input("name ")
        sPrice = input("price ")
        dictPrices[sName] = sPrice
        print(dictPrices)
    elif(sChoice == "2"):
        sName = input("name ")
        del dictPrices[sName]        
        print(dictPrices)
    elif(sChoice == "3"):
        for sName in dictPrices:
            print("Name is: " + sName + " Price is: "
                  + dictPrices[sName])
    else:
        break

```

5. Cash Register

```

class Item:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    def __str__(self):
        return(self.__name + "," + self.__price)
    def getName(self):
        return(self.__name)
    def getPrice(self):
        return(self.__price)


class CashRegister:
    def __init__(self):
        self.items = []
    def purchase_item(self, item):
        self.items.append(item)
    def show_items(self):
        print("Items in Cart")
        for item in self.items:
            print("   ", item)
    def get_total(self):
        nTotal = 0
        for item in self.items:
            nTotal += float(item.getPrice())
        return(nTotal)
    def clear(self):
        self.items = []

items = [Item("Jacket", "59.95"),
         Item("Designer Jeans", "34.95"),
         Item("Shirt", "24.95")]
cash = CashRegister()
nItem = 1

while nItem > 0:
    print("Please Enter an item to purchase. Enter 0 to checkout, C to clear")
    nItem = 0
    for item in items:
        nItem += 1
        print(nItem, item)
    sItem = input("please enter an item no >")
    if sItem.upper()  == "C":
        cash.clear()
        cash.show_items()
    else:
        try:
            nItem = int(sItem)
            if nItem > 0:
                cash.purchase_item(items[nItem - 1])
                cash.show_items()
        except:
            print("Please enter an item number, C or 0")

cash.show_items()
print("total:", cash.get_total())

```


6. Vowels, Consonants and word count

Question 3 +

```

aWords = sUserInput.split(" ")

print("The string has", len(aWords), "words")


```

7. Pig Latin

```
sInput = input("Enter an English phrase to translate")

aInput = sInput.split(" ")

sOutput = ""

for sWord in aInput:
    nFirst = 0
    for ch in sWord:
        if ch in "aeiou":
            break
        else:
            nFirst += 1
    if sOutput != "":
        sOutput += " "
    sOutput += sWord[nFirst:len(sWord)] + sWord[:nFirst] + "ay"

print(sOutput)


```

8. ISO 3166 Country codes

```
dictCountry = {"Argentina":"AR","Brazil":"BR","Canada":"CA", "Denmark":"DK", "Egypt":"EG", "France":"FR", "Germany":"DE", "Hungary":"HU", "India":"IN", "Japan":"JP"}

def getCountryCode(sCountry):
    global dictCountry
    return dictCountry[sCountry]

try:
    sCountryName = input("Enter the name of a country: ")
    sCountryCode = getCountryCode(sCountryName)
    print("The code for", sCountryName, "is", sCountryCode)
except:
    # there is a lot going on here!
    print("Please enter a country from", list(dictCountry.keys()))
```

9. Tossing a block

```
import random

class Block:
    def toss(self):
        aSides = ["D", "thank-you", "apple", "6", "car", "dog"]
        nSide = random.randint(0,5)
        return aSides[nSide]

oBlock = Block()

print(oBlock.toss())

```
