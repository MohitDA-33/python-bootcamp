# 2 - Write a program that keeps asking the user to enter a password until they enter the correct one.

password = "gk153"

entered_pass = input("enter password: ")

while(entered_pass != password):
    entered_pass = input("wrong password, try again: ")

print("successfully! logged in")
