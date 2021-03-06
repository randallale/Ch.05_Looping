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
while quit == False:
    print("1: Rock \n\r2: Paper \n\r3: Scissors \n\r4: Random\n\r5: Check Score \n\r6: Quit Game")
    answer = int(input())
    a = random.randrange(1, 4)  # Makes other "player's" choice
    if answer == 4: #Random generator
        answer = random.randrange(1,4)
    elif answer == 5:
        print("You won",player_score,"times")
        print("You lost",ai_score,"times")
        continue
    elif answer == 6:
        break
    if answer == 1:
        answer = "Rock"
    elif answer == 2:
        answer = "Paper"
    elif answer == 3:
        answer = "Scissors"
    if a == 1:
        a = "Rock"
    elif a == 2:
        a = "Paper"
    elif a == 3:
        a = "Scissors"
    print(answer,"vs.",a )
    if answer == a: #Checks both answers to see who wins
        print("Tie")
    elif answer.lower() == "scissors" and a.lower() == "paper": #Scissors vs. Paper
        player_score += 1
        print("You won!")
    elif answer.lower() == "paper" and a.lower() == "rock": #Paper vs. Rock
        player_score += 1
        print("You won!")
    elif answer.lower() == "rock"  and a.lower() == "scissors": #Rock vs. Scissors
        player_score += 1
        print("You won!")
    else:
        ai_score += 1
        print("You lost :(")
