'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random
heads = 0
tails = 0
times = 0
start = True
number = 0
while start == True:
    times += 1
    print(times)
    number = random.randrange(2)
    if number == 0:
        heads += 1
        number += 1
    else:
        tails += 1
    if number >= 20:
        start = False
        print(times)
