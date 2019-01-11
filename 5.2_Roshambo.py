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
quit = "n"
while quit == "n":
    answer = input("Rock, Paper, or Scissors? Or Random? \n\r")
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
    if answer.lower() == "rock" and a.lower() == "rock": #Checks both answers to see who wins
        print("Tie")
    elif answer.lower() == "scissors" and a.lower() == "scissors":
        print ("Tie")
    quit = input("Would you like to quit? \n\r")
    if quit.lower() == ("no"):
        quit = "n"
    elif quit.lower() == ("yes"):
        quit = "y"










