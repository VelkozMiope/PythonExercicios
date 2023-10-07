#    Number Guessing
#
#    Build a Number guessing game, in which the user selects a range.
#    Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
#    Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
#
import random
import math

def num_guess(first, last):
    random_number = random.randint(first, last)
    min_guess = math.log(last - first + 1, 2)
    
    print('You have', round(min_guess), 'chances!')
    
    count = 1
    while count < min_guess:
        
        guess = int(input('Your guess: '))

        if guess == random_number:
            print("Congratulations! You guessed in", count, "tries!")
            break
        elif guess < random_number:
            print("Wrong! You guessed too low!")
        else:
            print("Wrong! You guessed too high!")
        
        count+=1

    if count >= min_guess:
        print("Better luck next time!")
        print("The number was", random_number)

if __name__=="__main__":
    low = int(input('Input the lowest number: '))
    high = int(input('Input the highest number: '))
    num_guess(low, high)