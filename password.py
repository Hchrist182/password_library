#This file is the password library

#imports:
import random
import string

#strings that contain all of the necessary characters
lcase = string.ascii_lowercase
ucase = string.ascii_uppercase
spec_char = string.punctuation
num_char = string.digits



#creating the function
#this function takes in the length and 4 bool values to generate a password


def gen_random(length, lower_bool = True, upper_bool = True, spec_bool = True, num_bool = True):
    lst = []
    if length > 20 or length < 3:
        return 'the length needs to be between 3 and 20, try entering a different value.'
    if lower_bool == False and upper_bool == False and spec_bool == False and num_bool == False:
        return 'at least one of the bool values needs to be true, try entering different values.'
    for i in range(length):
        rng = random.randint(1,4)
        if rng == 1 and lower_bool == True:
            cc = random.choice(lcase)
        elif rng == 2 and upper_bool == True:
            cc = random.choice(ucase)
        elif rng == 3 and spec_bool == True:
            cc = random.choice(spec_char)
        elif rng == 4 and num_bool == True:
            cc = random.choice(num_char)
        lst.append(cc)
    password = ''.join(lst)
    print(password)


#Generates a password that isn't completely random it takes a user input
def gen(length, input, spec_bool = True, num_bool = True):
    if spec_bool == False and num_bool == False:
        return 'at least one of the bool values needs to be true, try entering different values.'
    lst = [input[:random.randint(1, len(input))]]
    for i in range(length-len(lst[0])):
        rng = random.randint(1, 2)
        if len(lst) >= length:
            return ''.join(lst)
        if rng == 1 and spec_bool == True:
            cc = random.choice(spec_char)
        elif rng == 2 and num_bool == True:
            cc = random.choice(num_char)    
        lst.append(cc)
    random.shuffle(lst)
    password = ''.join(lst)
    print(password)

#this function is a get help function, it will print strings describing the other functions
def get_help():
    print("""
    password is a small library that currently contains 2 generation functions. 
    here is a quick guide to using the provided functions:

    gen():
    the gen() function is used to generate a password given an input.
    choose an integer value and a string value. the integer will determine the length of the
    generated password. and the input will determine part of the password. the input will 
    be randomly sliced, and then surrounded by a random jumble of special characters
    and numbers. the spec_bool and num_bool arguments determine whether special or digit
    characters will be included. the default values for the bools are True.

    gen_random():
    the gen_random() function is used to generate a completely random password.
    similar to the gen() function, it takes an integer argument to determine the length
    of the password. the next four inputs are all bool values that determine the inclusion
    of lowercase, uppercase, special, and digit characters. the default values are set 
    to True.
    """)
