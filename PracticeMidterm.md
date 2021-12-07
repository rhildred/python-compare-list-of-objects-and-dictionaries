||||
|---|---|---|
||MB215 Practice Midterm||
|Name:|||
|Student Number:|||

Monday Dec. 6, 2021

Please solve 8 of the following 10 problems. Each solution is worth 10 marks. 
Create a working folder and save all of your .py files to the same folder. 
When your solutions are complete, please upload a .zip of that folder to the dropbox provided.

#### 1. Canadian Federal tax is calculated using the following formula:

![Federal tax schedule1](http://res.cloudinary.com/salesucation-com-inc/image/upload/v1508437770/Schedule1.png "Federal tax schedule1")

Write a program that asks the user for their taxable income and displays the result from line 44.

```
Please enter your taxable income> 165000
Your tax on 165000.0 is 36166.479999999996
```

#### 2. Volume of a cylinder

Write a program to calculate the volume of a cylinder. The user enters in the diameter of the end of the circle, and the height in meters:

volume = pi * r ** 2 * height 

    Input the radius and height
    Output the radius and height as they were input
    Output the volume of the cylinder

*Note: You will need to test for non-numeric input

##### Sample Output

```
radius >4
height >4
the volume is 201 cubic meters
```


#### 3. Vowels and Consonants

Write a program with a function that accepts a string as an argument and returns the number of vowels that the string contains. The application should have another function that accepts a string as an argument and returns the number of consonants that the string contains. The application should let the user enter a string and should display the number of vowels and the number of consonants it contains.

##### Sample Output

```
enter a string >The rain is raining over Spain
the string contains 11 vowels
the string contains 14 consonants
```

#### 4. Product Name and Price

Write a program that keeps product names and prices in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a product’s price, add a new product name and price, change an
existing price, and delete an existing product name and price.
Add a method to list all of the product names and prices in the dictionary.

##### Sample Output

```
0 - Exit
1 - Look up
2 - Add
3 - Change
4 - Delete
5 - List
Enter your choice >2
Enter Name >bread
Enter Price >$1.99
{'bread': '$1.99'}
0 - Exit
1 - Look up
2 - Add
3 - Change
4 - Delete
5 - List
```

#### 5. Cash Register

This exercise assumes that you have created the Item class from lab 7. Create a CashRegister class that can be used with the RetailItem class. The CashRegister class should be able to internally keep a list of RetailItem objects. The class should have the following methods:

* A method named purchase_item that accepts an Item object as an argument.
    Each time the purchase_item method is called, the RetailItem object that is passed as
    an argument should be added to the list.
* A method named get_total that returns the total price of all the Item objects stored in the CashRegister object’s internal list.
* A method named show_items that displays data about the RetailItem objects stored in the CashRegister object’s internal list.
* A method named clear that should clear the CashRegister object’s internal list.
* A method named add that allows the cashier to add a one of a kind item to the cash register
* A method named delete that allows the cashier to delete an item that is out of stock.

Demonstrate the CashRegister class in a program that allows the user to select several items for purchase. When the user is ready to check out, the program should display a list of all the items he or she has selected for purchase, as well as the total price.

##### Sample Output

```
Please Enter an item to purchase. Enter 0 to checkout, C to clear
1) Jacket, - 59.95
2) Designer Jeans - 34.95
3) Shirt - 24.95
a) Add an item
d) Delete an item
please enter an item no >f
Please enter an item number, C or 0
Please Enter an item to purchase. Enter 0 to checkout, C to clear
1) Jacket, - 59.95
2) Designer Jeans - 34.95
3) Shirt - 24.95
a) Add an item
d) Delete an item
please enter an item no >C
Items in Cart
Please Enter an item to purchase. Enter 0 to checkout, C to clear
1) Jacket, - 59.95
2) Designer Jeans - 34.95
3) Shirt - 24.95
a) Add an item
d) Delete an item
please enter an item no >2
Items in Cart
    2) Designer Jeans - 34.95
Please Enter an item to purchase. Enter 0 to checkout, C to clear
1) Jacket, - 59.95
2) Designer Jeans - 34.95
3) Shirt - 24.95
a) Add an item
d) Delete an item
please enter an item no >0
Items in Cart
    2) Designer Jeans - 34.95
total: 34.95
```

#### 6. Average calorie intake

Within a healthy, balanced diet, a man needs around 10,500kJ (2,500kcal) a day to maintain his weight. For a woman, that figure is around 8,400kJ (2,000kcal) a day.

Write a program that prompts the user to input the number of calories for 7 days and then prints the weekly average.

##### Sample Output

```
Enter your calories for day 1: 2490
Enter your calories for day 2: 2234
Enter your calories for day 3: 2768
Enter your calories for day 4: 2800
Enter your calories for day 5: 2900
Enter your calories for day 6: 2700
Enter your calories for day 7: 2200
Your average calories for 7 days was 2584.5714285714284
```

#### 7. Vowels, Consonants and word count

Write a program with a function that accepts a string as an argument and returns the number of vowels that the string contains. The application should have another function that accepts a string as an argument and returns the number of consonants that the string contains. A third function that is also required that looks counts the number of words in the sentence.

Hint Look for whitespace and punctuation

The application should let the user enter a string and should display the number of vowels, the number of consonants and the number of words that it contains.

```
enter a string >I am just a poor boy from a poor family. Spare me my life for this one atrocity.
the string contains 24 vowels
the string contains 38 consonants
the string contains 18 words
```

#### 8. Pig Latin

Write a program that accepts a sentence as input and converts each word to “Pig Latin.” In one version, to convert a word to Pig Latin you remove the letters up to the first vowel and place that letter at the end of the word. Then you append the string “ay” to the word. 
Here is an example:

English: I SLEPT MOST OF THE NIGHT

Pig Latin: IAY EPTSLAY OSTMAY OFAY ETHAY IGHTNAY

#### 9. ISO 3166 Country codes

Write a program that uses a dictionary to map 10 country names to their ISO 3166 2 letter code. Use an exception to make sure that if the country name isn't in the dictionary it returns a helpful error message.

#### 10. Tossing a block

A child's block has a letter D on one face, the word thank-you on another, a picture of an apple on another, the numeral 6 on another, a car on another and a dog on the 6th face. Write a program that tosses that block and reports the side that is up when the block comes to a rest.

## (Partial) Solutions

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

6. Average Calorie intake

```
nTotal = 0
nDays = 7

for n in range(1, nDays + 1):
    nTotal += int(input("Enter your calories for day " + str(n) +": "))
print("Your average calories for", nDays, "days was", nTotal/nDays)
                  
```

7. Vowels, Consonants and word count

Question 3 +

```

aWords = sUserInput.split(" ")

print("The string has", len(aWords), "words")


```

8. Pig Latin

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

9. ISO 3166 Country codes

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

10. Tossing a block

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
