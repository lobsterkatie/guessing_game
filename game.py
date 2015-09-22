import random

print "Welcome to our guessing game!"
print "What is your name?"
user_name = raw_input(">")

secret_number = random.randint(1,100)

while True:
    user_guess = int(raw_input("Guess a number: "))
    if user_guess > secret_number:
        print "Too high"
    elif user_guess < secret_number:
        print "Too low"
    else: 
        print "You guessed it!"
        break
