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