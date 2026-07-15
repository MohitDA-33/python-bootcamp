# lucky roulette/draw

num = int(input("Choose a number between 1 to 100: "))

if (num == 10):
    print("You won a million dollar $")

elif(num == 79):
    print("You won a house")

elif(num == 40):
    print("You won a car")

else:
    print("better luck next time")

'''
Its a roulette/draw game created by using if, elif and else statement.
What this program does is it goes condition by condition matching the value, and if the value fits the condition,
it prints the argument matching the condition. otherwise better luck next time!.
'''
# But in these types of conditions its better to use matchcase, cause its much more convenient.