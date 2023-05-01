# GAME - HANGMAN

import random
'''import hangman_words'''

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

'''def Input():
    word_list = hangman_words.word_list
    word = (word_list[random.randint(0,len(word_list)-1)])
    Input.wrd = list(word)
    length = len(word)
    Input.dash_list = []
    for i in range(0,length):
        Input.dash_list.append("_")
    print(logo)
    print("\n")    
    print("Total guesse : 6") 
    print(stages[6])   
    print(Input.dash_list)

def checking():
    all_done = False
    t = 5
    while not all_done:
        Input.x = input("Guess the word : ")
        a=0
        for i in Input.wrd:
            if i == Input.x :
                Input.dash_list[a] = Input.wrd[a]
                a+=1
            else :
                a+=1

        if Input.x not in Input.wrd :
            t -= 1 

        print(stages[t+1])
        print("Guess left : ",t+1)

        if t == -1:
            print("You loose.")
            print(f"The correct word is : {Input.wrd}")
            all_done = True 

        if "_" not in Input.dash_list:
            all_done = True
            print("YOU WON!!!")

        print(f"You guessed : {Input.dash_list}")

Input()
checking()'''