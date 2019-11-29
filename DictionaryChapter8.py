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
