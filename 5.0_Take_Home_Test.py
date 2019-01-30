'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Alexander Randall


1. Write a Python program that will use a FOR loop to print your name
     10 times, and then the word Done at the end.
 '''  
for i in range(10):
    print("Alex ;)")
print("Done")

'''
  2. Write a Python program that will use a FOR loop to print Blue
     and then White 20 times. (Blue White Blue White Blue White... all on separate lines.
     Don't use \n.)
'''
for i in range(20):
    print("Blue")
    print("White")

'''
  3. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(1,51):
    print(i*2)


'''
  4. Write a Python program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
number = 10
while True:
    print(number)
    number -= 1
    if number == -1:
        print("Blast off!")
        break
        #Or I could set a variable to the while loop and set it to false after the if statement

''' INCORRECT. This program is not printing the total.
  5. There are three things wrong with this program. List each.
     
     print("This program takes three numbers and returns the sum.")
     total = 0

     for i in range(3):
         x = input("Enter a number: ")
         total = total + i
     print("The total is:", x)
'''
#1: X needs to be an integer so you need to do int(input("Enter a number: "))
#2: 
#3: Instead of the i in the total = total + i you would need to use the x variable
'''
  6. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
print(random.randrange(1,11))

'''
  7. Write a program that prints a random floating point number somewhere between
     1 and 10 (inclusive). Do not make the mistake of generating a random number from
     0 to 10 instead of 1 to 10.
'''
import random
print(random.random()*10+1) # 1-11 You need 1-10


'''
  8. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the number entries equal to zero,
     and the number of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
number = 0
positive = 0
negative = 0
zero = 0
for i in range(7):
    x = int(input("Enter a number: "))
    number += x
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1
    else:
        zero += 1
print("The sum is",number)
print("You had",positive,"positive numbers.")
print("You had",negative,"negative numbers.")
print("You had",zero,"zeros.")
