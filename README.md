This text file contains all necessary information for working the password library.

About the author:
Call me Hank. This is my first ever project, so chances are that this really sucks. If you have any feedback, please provide it.

Importing:
Download the password.py file and move into the directory that contains the working file.
Use the import syntax and go from there.

get_help():
This function prints a body of text to the terminal describing the gen() and gen_random( functions)

gen():
The gen() function is used to generate a password given an input.
Choose an integer value and a string value. The integer will determine the length of the
generated password and the input will determine part of the password. The input will 
be randomly sliced, and then surrounded by a random jumble of special characters
and numbers. The spec_bool and num_bool arguments determine whether special or digit
characters will be included. The default values for the bools are True.

gen_random():
The gen_random() function is used to generate a completely random password.
Similar to the gen() function, it takes an integer argument to determine the length
of the password. The next four inputs are all bool values that determine the inclusion
of lowercase, uppercase, special, and digit characters. The default values are set to True.

general info:
This library uses imports from random, and string. Everything is written in python
and performance can suffer as a result. Because of this, the functions will not generate
anything larger than 20 characters. There is also a minimum of 3 characters for the sake
of generating useful passwords.
