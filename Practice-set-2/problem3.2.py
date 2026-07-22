# 2 - Print the multiplication table of a number (entered by user).

a = int(input("Enter your number here: "))

for num in range(1, 11):
    print( a,"x",num,"=", a*num)