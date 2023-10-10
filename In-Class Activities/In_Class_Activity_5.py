"""
Hannah Wilkinson
09.27.2023
"""
import IfStatement
import In_Class_3

#print()
activity = input("Which in class activity would you like to run?")
userInput = input('1' or '2' or '3')

def inputData(input):
    if (input == '1'):
        IfStatement()
        print(activity)
        print(IfStatement())
        #userInput = input(IfStatement())

def classActivity(activity):
    if (activity == "1"):
        IfStatement()
        print(activity)
        userInput = input(IfStatement())

    elif (activity == "3"):
        (In_Class_3())

    #else (activity == "4"):
        #In-Class-4-Pinger()

#print(activity)

