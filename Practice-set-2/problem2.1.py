# Match Case Statements

# 1 - Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.

day = int(input("Enter a number between 1 - 7, to print the corresponding day of the week\n"))

match day:
    case 1 :
        print("Sunday")

    case 2 :
        print("Monday")

    case 3 :
        print("Tuesday")

    case 4 :
        print("Wednesday")

    case 5 :
        print("Thursday")

    case 6 :
        print("Friday")

    case 7 :
        print("Saturday")