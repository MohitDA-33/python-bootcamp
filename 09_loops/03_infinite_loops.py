# i = 1

# while i < 6 :
#     print(i)
#     i = i + 1

# You know what this does, but if i remove the i in (i = i + 1) or think that i forgot to write it, what will happen is, this program run but will never update the value of i =, which means the value of i will always be 1, which in turn will keep executing, now it will start printing 1111... till my system crashes or hangs, or you can say its gets stuck in the loop, not able to update the value.

i = 1

while i < 6 :
    print(i)
    i + 1

# These types of mistakes can end you up in an infinite loop.

# while True creates an infinite loop because the condition is always True, since the condition never becomes False, the loop keeps running, until the program is stopped manually.

i = 1
while True:
    print(i)
    i = i + 1

# What it does, it will start printing 123456789.. till my system crashes or hangs up.
