# While loops ? While loop executes a block of code as long as a condition is true 

# Syntax:
# While condition:
     # Code to execute while condition is true

# Example: It prints from 1 to 5
i = 1

while i < 6:
    print(i)
    i = i + 1

# What happens here is, the value of i is 1, then its goes to the while condition and checks if the condition is true, in this case 1 < 6 so thats true, after this its prints i which is 1, then what happens it goes to second line of code i = i + 1 which updates the value, so now the value of i = 1 + 1, i = 2, and then it goes in the loop till the condition is not matched, it will stop after 5 cause, 6 < 6 is not true.

# It prints from 399-500
a = 399

while a < 501:
    print(a)
    a = a + 1

# Another example: Print the multiplication table of 19.
multiple = 19

while multiple < 191:
    print(multiple)
    multiple +=19

# Backward multiplication table of 7.
num = 70
while num > 6:
    print(num)
    num = num - 7

# What happens here is num = 70, the while condition is checked num > 6 if its true, then it prints the num and update the value till its greater than 6 , this time its backward, the value drops everytime by 7 creating a loop like a backward multiplication of 7.