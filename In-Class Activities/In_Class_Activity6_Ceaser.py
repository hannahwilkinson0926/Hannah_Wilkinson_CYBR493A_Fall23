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
encryptionIndex = {'a', 'b', 'c', 'd,', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z'}
text = ""
key = 2
print(encryptionIndex)

for char in text:
    value = encryptionIndex.index(char)
    inputNew = input + key
    print (inputNew)
    newValue = value + key
    print(newValue)