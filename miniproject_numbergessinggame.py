import random

secret_number = random.randint(1, 10)

attempts = 3

print("I'm thinking of a number 1 and 10")

while attempts>0: 
    guess = int(input("take a Gess: "))
    if guess== secret_number:
        print("Congratulations ! You guessed the number!")
        break
    elif guess< secret_number:
        print("Too low! try again!!!.")
    else:
        print("too high! Try again!!!.")
    attempts-=1

if attempts ==0:
    print("Sorry, you've run out of attempts. the secret number was: ",secret_number)
    