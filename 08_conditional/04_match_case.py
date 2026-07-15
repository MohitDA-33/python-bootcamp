# Match case is a new feature introduced in python 3.10 for patter matching

'''
How it works,
the value of the variable is matched with the no of cases present and then prints the argument/statement against it,
otherwise if no case matches it will print the default case.
'''
# Example: roulette/draw game

num = int(input("Enter a number between 1 to 10: "))

match num:
    case 1:
        print("Congrats you won a Charger")

    case 2:
        print("Congrats you won 5$")

    case 9:
        print("You get one more chance to pick a number")
        num = int(input("Again pick a number between 1 to 10: "))
        match num:
            case 3:
              print("You get 1$")

            case 4:
              print("You get 2$")

            case _:
              print("Oops! better luck next time")

    case _:
        print("Oops better luck next time")

'''
What this program does is, when you enter a number as an input it stores itself in the variable, 
and then the value of that variable gets matched with the no of cases one by one, 
if it matches then Okay otherwise it prints the Default case.
'''