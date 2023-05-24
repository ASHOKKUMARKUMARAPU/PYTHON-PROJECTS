import random
import math

# taking inputs

lower = int(input("Enter your lower boundary:"))
upper = int(input("Enter your upper boundary:"))

# generating random number between the boundaries

x = random.randint(lower,upper)
print("You've only ",
      round(math.log(upper - lower +1,2)),
      " chances to guess the integer")

# Initializing the no.of guesses

count = 0

# calculation of min no. of guesses

while count <= math.log(upper - lower +1,2):
    count +=1
    guess = int(input("guess a number:"))

    if x == guess:
        print("Congratulations you did it in ",count," try")
        break
    elif x > guess:
        print("you guessed too small!")
    elif x < guess:
        print('you guessed too high!')


# if guessing is more than required guesses

if count > math.log(upper - lower +1,2):
    print("Better luck next time!","The number is", x)






