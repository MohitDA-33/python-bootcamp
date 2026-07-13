# The print() statement\function is used to display output given as an argument.
# From the last topic, there is also a different way to have or use double quote or single quote. other than using a escape sequence.
'''
print("This is how you put a single quote ' you have to use it between double quotes")
'''
# Vice versa
'''
# print('This is how you put a double quote " you have to use it between single quotes')
'''
# Print statements prints anything that you give it as an argument.

# (sep) and (end) paramters

print("Hello", "world", 5, sep=",")
# By default when you pass multiple arguments in single print function it gives spaces in between, but by using sep(seperator) you can define how to seperate the arguments in this case its a (,).

print("Hello world", end="..")
print("Hello python", end="..")
print("Hello Mohit")
# End parameter, by default end paramater is a new line(\n) so what it does is when you give multiple print statements,
# when one print statement is finished giving the output, it starts the other one in the next line. what i have done is i have used to end parameter as = .. , 
# so now what it does is it dosent starts with a new line it starts the second print statement after double dots. 