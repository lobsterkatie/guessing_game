import random

#main guessing-game logic
def main():
    print "Welcome to our guessing game!"
    print "What is your name?"
    user_name = raw_input(">")
    print "Hello, {}!".format(user_name)

    secret_number = random.randint(1,100)   

    while True:
        user_guess = get_user_input()
        if user_guess > secret_number:
            print "Too high"
        elif user_guess < secret_number:
            print "Too low"
        else: 
            print "You guessed it!"
            break


#check to see if the given string is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


#get and error-check user input for guess
def get_user_input():
    input_valid = False;

    #keep asking for input until user inputs valid entry
    while not input_valid:
        user_guess_str = raw_input("Guess a whole number: ")

        #if entry isn't numeric, protest and ask again
        if not is_number(user_guess_str):
            print "Please enter a NUMBER"
            continue

        #if entry contains a decimal point, protest and ask again
        if user_guess_str.find(".") != -1:
            print "Please enter a WHOLE number"
            continue

        #if this is reached, entry *is* integral and can be
        #cast to an int
        user_guess = int(user_guess_str)

        #check entry against specified range
        if user_guess < 1 or user_guess > 100:
            print "Please make sure your number is in [1,100]"
            continue

        #otherwise, entry is valid!
        input_valid = True

    return user_guess


main()
