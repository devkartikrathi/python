# ROCK PAPER SCISSORS

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

x= int(input("Enter 0 for rock, 1 for paper or 2 for scissors :  \n"))
y = random.randint(0,2)
def checking(x,y):
    if x>2 and x<0:
        print("You chose wrong number, You loose.")
    elif x == y:
        print("It's a draw.")
    elif x>y:
        print("You win.")
    else:
        print("You loose")

checking(x,y)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# WHO WILL PAY?

import random

all_name = input("Give me name of all the persons. \n")
#now splitting all name into a list
name = all_name.split(", ")
x = len(name)
y =  random.randint(0,x-1)

print(name[y], "will pay the bill.")

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
