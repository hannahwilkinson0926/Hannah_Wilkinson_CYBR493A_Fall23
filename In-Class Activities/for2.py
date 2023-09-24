#import maskpass
import getpass
#import matplotlib

data = getpass.getpass('\nPassword:')
print(data)

#passwordInput = maskpass.askpass(prompt="Hello user, give me a password:", mask="*")
#guess = False

#while data is False:
    #passwordGuess = input("Ok, what is the reversed password? I will keep asking until you")

passwordInput = input("What is 3 * 4\n")
guess = False
while guess is False:
    passwordGuess = input ("try again\n")
    if (input == (3*4)):
        guess = True
print ("You got it!")

passwordInput = input("Give me a password\n")
guess = False
while guess is False:
    passwordGuess = input ("Ok, what is the reversed password?")
    if (''.join(reversed(passwordGuess))) == passwordInput:
        guess = True
print ("You got it!")