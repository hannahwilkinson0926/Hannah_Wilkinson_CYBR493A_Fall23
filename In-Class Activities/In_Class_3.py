def main():
    print()
    userInput = input("Guess the password")
    if WordsCheckerWithInput(userInput) == True:
        print("Moving to the next functionality")
    else:
        print("You are stuck here")

    #strTemp = "Fluffkinz"
    #CoolWordsChecker()
    #if WordsChecker.userInput == "Fluffkinz":
        #print("This is a new funcionality")

    if CoolWordsChecker() == True:
        print("Moving to next funcionality")
    else:
        print("You're stuck here")

def WordsCheckerWithInput(data):
    """
    This method checks whether data matches the password
    :param data: This is what is being passed from the main method
    :return:
    """
    if (data =="Fluffkinz"):
        return True
    else:
        return False

def CoolWordsChecker():
    """
    This method tells whether a user input matches a pre-defined password or not
    :return: True if passwords match, False if not.
    """
    secretword = "Fluffkinz"
    userInput = input("Guess the password")
    if (secretword == userInput):
        #print ("You guessed it")
        return True
    else:
        return False
        #print ("You did not guess the password")

if __name__ == "__main__":
    main()