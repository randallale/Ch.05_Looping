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
instructions = int(input("Would you like instructions?\n\r1: Yes\n\r2: No\n\r"))
if instructions == 1: #Are instructions
    print("Welcome to the Millennium Falcon. It's the ship that made the Kessel run in less than 12 parsecs.")
    print("The object is to travel 200 Solar Systems across the Galaxy to safety.")
    print("A squad of imperial troopers will be chasing you.")
    print("You will be asked for commands every so often.")
while not done: #Main loop

    #Prints Commands
    print("\n\t\tCommands")
    print("A. Drink your supply of green milk.")
    print("B. Move at a moderate speed.")
    print("C. Punch it Chewie")
    print("D. Repair the Millennium Falcon")
    print("E. Status check.")
    print("Q. Quit")
    user_choice = input("\n\rWhat is your command?\n\r")

    #Checks users choice and acts accordingly

    if user_choice.upper() == "Q": #Main if statements
        print("Goodbye!")
        break
    elif user_choice.upper() == "E":
        print("Solar systems traveled: ",miles_traveled)
        print("Drinks on the Millennium Falcon: ",drinks)
        print("The Imperials are",(miles_traveled-natives_traveled),"Solar Systems behind you")

    elif user_choice.upper() == "D":
        camel_tiredness = 0
        natives_traveled += random.randrange(7,15)
        if not natives_traveled >= miles_traveled:
            print("The Millennium Falcon hyperdrive is fully repaired")


    elif user_choice.upper() == "C":
        miles_traveled += random.randrange(10,21)
        print("You have traveled",miles_traveled,"solar systems")
        thirst += 1
        camel_tiredness += random.randrange(1,4)
        natives_traveled += random.randrange(7,15)

    elif user_choice.upper() == "B":
        miles_traveled += random.randrange(5,13)
        print("You have traveled",miles_traveled,"solar systems")
        thirst += 1
        camel_tiredness += 1
        natives_traveled += random.randrange(7, 15)

    elif user_choice.upper() == "A":
        if drinks >= 1:
            drinks -= 1
            thirst = 0
        else:
            print("You don't have green milk left on the ship")

    #Checking players stats

    if thirst > 6:
        print("You died of thirst")
        break
    elif thirst > 4 and not natives_traveled >= miles_traveled and not camel_tiredness > 8:
        print("You are thirsty for some green milk.")

    if camel_tiredness > 8 and not thirst > 6:
        print("The Millennium Falcon was destroyed")
        break

    elif camel_tiredness > 5 and not thirst > 6 and not natives_traveled >= miles_traveled:
        print("The Millennium Falcon's hyperdrive is starting to go bad")

    if natives_traveled >= miles_traveled and not miles_traveled >= 200:
        print("The Imperials caught you!")
        break
    elif miles_traveled >= 200:
        print("You won the game!")
        break
    elif natives_traveled >= (miles_traveled-15):
        print("The Imperials are close!")

    if random.randrange(1,21) == 1:
        print("You a Cantina!")
        drinks = 6
        thirst = 0
        camel_tiredness = 0