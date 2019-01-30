'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_traveled = -20
drinks = 6
instructions = int(input("Would you like instructions\n\r1: Yes\n\r2: No\n\r"))
if instructions == 1: #Are instructions
    print("Welcome to Camel. The object is to travel 200 miles across the great Gobi Desert.")
    print("A tribe of knocked kneed pygmies will be chasing you.")
    print("You will be asked for commands every so often.")
while not done: #Main loop

    #Prints Commands
    print("\n\t\tCommands")
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed")
    print("D. Stop for the night")
    print("E. Status check.")
    print("Q. Quit")
    user_choice = input("\n\rWhat is your command\n\r")

    #Checks users choice and acts accordingly

    if user_choice.upper() == "Q": #Main if statements
        print("Goodbye!")
        break
    elif user_choice.upper() == "E":
        print("Miles Traveled: ",miles_traveled)
        print("Drinks in canteen: ",drinks)
        print("The natives are",((natives_traveled)*-1),"miles behind you")

    elif user_choice.upper() == "D":
        camel_tiredness = 0
        print("You're camel is happy")
        natives_traveled += random.randrange(7,15)

    elif user_choice.upper() == "C":
        miles_traveled += random.randrange(10,21)
        print("You have traveled",miles_traveled,"miles")
        thirst += 1
        camel_tiredness += random.randrange(1,4)
        natives_traveled += random.randrange(7,15)

    elif user_choice.upper() == "B":
        miles_traveled += random.randrange(5,13)
        print(miles_traveled)
        thirst += 1
        camel_tiredness += 1
        natives_traveled += random.randrange(7, 15)

    elif user_choice.upper() == "A":
        if drinks >= 1:
            drinks -= 1
            thirst = 0
        else:
            print("You don't have any drinks left in your canteen.")

    #Checking players stats

    if thirst > 6:
        print("You died of thirst :(")
        done = True
    elif thirst > 4:
        print("You are thirsty.")

    if camel_tiredness > 8 and not thirst > 6:
        print("Your camel is dead.")

    elif camel_tiredness > 5 and not thirst > 6:
        print("Your camel is getting tired")

    if natives_traveled >= miles_traveled:
        print("The natives caught you!")
        break

    elif natives_traveled < 15:
        print("The natives are getting close!")

    if miles_traveled >= 200:
        print("You won the game!")
        break

    if random.randrange(1,21) == 1:
        print("You found an oasis!")
        drinks = 6
        thirst = 0
        camel_tiredness = 0