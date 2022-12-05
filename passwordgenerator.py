#password generator

import random

print('welcome to your password generator')

#generatorating random letters and symbols
chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

#new variable takes number of passwords we want to generate
number = input('Amount of passwords to generate: ')
number =int(number)

#length is length of the password, the input we put earlier
length = input('Input your password length: ')
# we want to make sure we get an integer from the user
length = int(length)

print('here are your passwords')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    #giving random choice, text from the striong and past it in string
    print(passwords)