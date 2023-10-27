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
        print(location)

        if (location == 0 or 5 or 10 or 15 or 20 or 25):
            print("%")
        elif (location == 1 or 6 or 11 or 16 or 21 or 26):
            print("&")
        elif (location == 2 or 7 or 12 or 17 or 22):
            print("$")
        elif (location == 3 or 8 or 13 or 18 or 23):
            print("*")
        elif (location == 4 or 9 or 14 or 19 or 24):
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