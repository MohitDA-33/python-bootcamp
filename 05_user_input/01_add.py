# This time we will take user input and then add the numbers.

'''
a = input("enter your first number: ")
b = input("enter your second number: ")

print(a+b)
'''

# It will not add it, cause the input is taken as a string, and strings dont add up to each other. they have to be integers.
# One more example

'''
a = input("enter your number: ")
print(a+3)
'''

# It will show error. why? cause a is a string and 3 is an integer, and string and integer dont add up each other.
# To fix this issue we will use typecasting

# Revised code/program
a = input("enter your number: ")
a =int(a)
print(a+3)

# What it will do is it will treat it as an integer rather than as a string.

# One more example
a = input("enter your first number: ")
b = input("enter your second number: ")

a = int(a)
b = int(b)

print(a+b)

# One more way of doing this, but this we are going to subtract the numbers.

a = int(input("enter your first number: "))
b = int(input("enter your second number: "))

print(a-b)

'''
How python interprets: when you enter the value/number it enters as a string, but then that string is converted into an integer
'''

# And in total there are 3 working examples. the first 2 are just to demonstrate, you can uncomment and see whats wrong in that. 