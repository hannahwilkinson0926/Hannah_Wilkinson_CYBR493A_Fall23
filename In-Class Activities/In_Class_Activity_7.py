"""
Hannah Wilkinson
10.11.2023
"""

import string
def main():
    """

    :return:
    """
    welcomeString = input("Please enter a value you would like to encrypt:")
    encryptionIndex = ['a', 'b', 'c', 'd,', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                       'u', 'v', 'w', 'x', 'y', 'z']
    text = ""
    key = 2
    print(encryptionIndex)
    print("String to be encrypted: " + welcomeString)
    for char in welcomeString:
        location = encryptionIndex.index(char)
        #print(location)

        if (location == 0):
            print("%")
        elif (location == 1):
            print("&")
        elif (location == 2):
            print("$")
        elif (location == 3):
            print("*")
        elif (location == 4):
            print("^")
        else:
            print("None")

        #if ('a' in welcomeString):
            #print('%')
        #elif ('b' in welcomeString):
            #print('#')
        #elif ('c' in welcomeString):
            #print('&')

        #print(location)
        # inputNew = input + key
        # print(inputNew)
        # newValue = value + key
        # print(newValue)
if __name__ == "__main__":
    main()