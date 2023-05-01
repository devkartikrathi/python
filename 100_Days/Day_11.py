# NUMBER GUSSING

import random

def game():
    def checking(guesses_left):
        guesses_left = guesses_left-1
        guess_left = guesses_left 
        if guess_left > -1:
            x = int(input("Enter number : "))
            if x == num:
                print("Congratilation you've guessed the number.")
                y = input("Do you want to play again 'Y' or 'N' : ")
                if y == "y" or y == "Y":
                    game()
                else:
                    print("Thanks for playing.")
            else:
                if x > num:
                    print("Your guess is too high.")
                    print("Guesses Left : ",guesses_left)
                    checking(guesses_left)
                else:
                    print("Your guess is too low.")
                    print("Guesses Left : ",guesses_left)
                    checking(guesses_left) 
        else:
            print("You are out of chances.")
            print("The number was : ",num)
            y = input("Do you want to play again 'Y' or 'N' : ")
            if y == "y" or y == "Y":
                game()
            else:
                print("Thanks for playing.") 

    def easy():
        guesses_left = 10
        print("Guesses Left : ",guesses_left)
        checking(guesses_left) 

    def hard():
        guesses_left = 5
        print("Guesses Left : ",guesses_left)   
        checking(guesses_left) 

    num = random.randint(1,100)

    diff_ = input("Choose the difficulty level, type 'easy' or 'hard' : ")
    diff = diff_.lower()

    if diff == 'hard':
        hard()
    elif diff == 'easy':
        easy()    
    else:
        print("Your choice is invalid.")

game()