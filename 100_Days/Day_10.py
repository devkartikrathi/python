#Blackjack

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ttl(user_choice, pc_choice):
    user_total = 0
    for choice in user_choice:
        user_total += choice
    pc_total = 0    
    for choice in pc_choice:
        pc_total += choice
    return(user_total, pc_total)    

def pt(user_total, pc_total):
    if user_total > 21:
        print("YOU LOOSE")
        mandat(user_choice, pc_choice, user_total, pc_total)
    elif user_total == pc_total:
        print("It's a draw")
        mandat(user_choice, pc_choice, user_total, pc_total)    
    elif user_total > pc_total:
        print("YOU WIN")
        mandat(user_choice, pc_choice, user_total, pc_total)
    else:
        print("YOU LOOSE")
        mandat(user_choice, pc_choice, user_total, pc_total)

def mandat(user_choice, pc_choice, user_total, pc_total):
    print("Your cards : ",user_choice)
    print("PC's cards : ",pc_choice)
    print("User total is : ", user_total)
    print("PC total is : ", pc_total)        

user_choice =[]
pc_choice = []

for i in range(2):
    user_choice.append(random.choice(cards))
    pc_choice.append(random.choice(cards))

print("You get : ", user_choice)
print("One of the PC's card is :", pc_choice[0])
x = input("If you want to hit press 'Y' else 'N' : ")
if x == "Y" or x == "y":
    user_choice.append(random.choice(cards))
    user_total, pc_total = ttl(user_choice, pc_choice)
    pt(user_total, pc_total)
else:
    user_total, pc_total = ttl(user_choice, pc_choice)
    pt(user_total, pc_total)