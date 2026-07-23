# Pass statements:

# A few examples showing how pass statements works in for loop:

# Sometimes when you want to write a piece of code later, we write pass statement or pass:

# Example:
for i in range(2, 11, 2):
    if i == 6:
        pass # do nothing
    print(i)

# The pass statement is a placeholder that does nothing. it is used when a syntax requires a statements but no action is needed or if you feel like not writing something inside if statement and you plan to write it later you can use pass statement.

for z in range(1, 21, 1):
    if z == 11:
        pass
    print("zzz"*z)

# The pass statement doesn't skip the current iteration. here print(i) and print(z) will run anyways.

# Another example:
a = 12
b = 15

if a > b :
    pass

else:
    print("false")