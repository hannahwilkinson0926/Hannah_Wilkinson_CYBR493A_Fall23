"""
Hannah Wilkinson
10.9.2023
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

if __name__ == "__main__":
    main()