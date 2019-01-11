'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

import random
quit = False
player_score = 0
ai_score = 0
endingloop = False
while quit == False:
    endingloop = False # Makes sure the loop is on at the end
    print("1: Rock \n\r2: Paper \n\r3: Scissors \n\r4: Random")
    answer = input()
    if answer.lower() == "random": #Random generator
        answer = random.randrange(1,4)
        if answer == 1:
            answer = "Rock"
        elif answer == 2:
            answer = "Paper"
        elif answer == 3:
            answer = "Scissors"
    a = random.randrange(1, 4) # Makes other "player's" choice
    if a == 1:
        a = "Rock"
    elif a == 2:
        a = "Paper"
    elif a == 3:
        a = "Scissors"
    print(answer,"vs.",a )
    if answer.lower() == a.lower(): #Checks both answers to see who wins
        print("Tie")
    elif answer.lower() == "scissors" and a.lower() == "paper":
        player_score += 1
        print("You won!")
    elif answer.lower() == "paper" and a.lower() == "rock":
        player_score += 1
        print("You won!")
    elif answer.lower() == "rock" and a.lower() == "scissors":
        player_score += 1
        print("You won!")
    else:
        ai_score += 1
        print("You lost :(")
    while endingloop == False: # Makes a loop incase the player puts a random term as an answer
        quit = input("Would you like to quit? \n\r")
        if quit.lower() == ("no"):
            quit = False
            endingloop = True
        elif quit.lower() == ("yes"):
            quit = True
            endingloop = True
            print("You won",player_score,"times")
            print("You lost ",ai_score,"times")
