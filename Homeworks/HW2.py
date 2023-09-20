"""
Hannah Wilkinson
HW #2
9.20.23
CYBR493A-001
This program will take the user input (password) and check to see if it fits all the requirements below.
"""

"""
   This method checks whether the password is 8 characters or more.
"""
def ValidLength(password):
    if len(password) >= 8:
        return True
    else:
        return False

"""
   This method checks whether the password has at least one number.
"""
def HasNumber(password):
    if ('1' in password) or ('2' in password) or ('3' in password) or ('4' in password) or ('5' in password) or ('6' in password) or ('7' in password) or ('8' in password) or ('9' in password) or ('0' in password):
            return True
    else:
        return False

"""
   This method checks whether there is at least one symbol in the password.
"""
def HasSymbol(password):
    if('%' in password) or ('!' in password) or ('@' in password) or ('#' in password) or ('$' in password) or ('&' in password) or ('*' in password):
        return True
    else:
        return False