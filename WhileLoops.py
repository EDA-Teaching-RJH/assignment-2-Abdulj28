### Part Two -- your code goes here. 
import random

print("guess a number between 1-100")

snumber = random.randint(1,100)




while True:
    gval = int(input("number:"))

    if snumber>gval:
        print("guess is too low, guess again")

    elif snumber<gval:
        print("guess is too high, guess again")

    else:
        print(gval, "is correct")
        break













