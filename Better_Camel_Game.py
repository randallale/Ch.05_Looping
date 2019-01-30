'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
import time
done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_traveled = -20
drinks = 6
print("A long time ago in a galaxy far, far away....")
time.sleep(2)
print("\n\t\t\tStar Wars")
time.sleep(1)
print("\t\t\tEpisode V")
time.sleep(1)
print("\tThe Empire Strikes Back\n\n")
time.sleep(2)
print("It is a dark time for the Rebellion.")
time.sleep(2)
print("Although the Death Star has been destroyed,")
time.sleep(2)
print("Imperial troops have driven the Rebel forces")
time.sleep(2)
print("from their hidden base and pursued them across")
time.sleep(2)
print("the galaxy. Evading the dreaded Imperial Starfleet,")
time.sleep(2)
print("the Millennium Falcon must get to Hoth\n\n")
time.sleep(4)
instructions = int(input("Would you like instructions?\n\r1: Yes\n\r2: No\n\r"))
if instructions == 1: #Are instructions
    print("Welcome to the Millennium Falcon. It's the ship that made the Kessel run in less than 12 parsecs.")
    print("The object is to travel 200 Solar Systems across the Galaxy to Hoth.")
    print("A Imperial Starfleet will be chasing you.")
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
        print("Do.")
        time.sleep(1)
        print("Or do not.")
        time.sleep(1)
        print("There is no try.")
        break
    elif user_choice.upper() == "E":
        print("Solar systems traveled: ",miles_traveled)
        print("Drinks on the Millennium Falcon: ",drinks)
        print("The Imperial Starfleet is",(miles_traveled-natives_traveled),"Solar Systems behind you")

    elif user_choice.upper() == "D":
        camel_tiredness = 0
        natives_traveled += random.randrange(7,15)
        if not natives_traveled >= miles_traveled:
            print("The Millennium Falcon hyperdrive is fully repaired")


    elif user_choice.upper() == "C":
        miles_traveled += random.randrange(10,21)
        print("You have traveled",miles_traveled,"Solar Systems")
        thirst += 1
        camel_tiredness += random.randrange(1,4)
        natives_traveled += random.randrange(7,15)

    elif user_choice.upper() == "B":
        miles_traveled += random.randrange(5,13)
        print("You have traveled",miles_traveled,"Solar Systems")
        thirst += 1
        camel_tiredness += 1
        natives_traveled += random.randrange(7, 15)

    elif user_choice.upper() == "A":
        if drinks >= 1:
            drinks -= 1
            thirst = 0
        else:
            print("You don't have any green milk left on the ship")

    #Checking players stats

    if thirst > 6:
        print("You died of thirst")
        print("Ive never been a bad boy")
        break
    elif thirst > 4 and not natives_traveled >= miles_traveled and not camel_tiredness > 8:
        print("You are thirsty for some green milk.")

    if camel_tiredness > 8 and not thirst > 6:
        print("The Millennium Falcon was destroyed")
        print("That's not how the Force works!")
        break

    elif camel_tiredness > 5 and not thirst > 6 and not natives_traveled >= miles_traveled:
        print("The Millennium Falcon's hyperdrive is starting to go bad")

    if natives_traveled >= miles_traveled and not miles_traveled >= 200:
        print("The Imperial Starfleet caught you!")
        print("Marching into a detention area is not what I had in mind.")
        break
    elif miles_traveled >= 200:
        print("You won the game!")
        print("Chewie, we're home.")
        break
    elif natives_traveled >= (miles_traveled-15):
        print("The Imperial Starfleet is close!")

    if random.randrange(1,21) == 1:
        print("You found a Cantina!")
        drinks = 6
        thirst = 0
        camel_tiredness = 0