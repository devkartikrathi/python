def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is it like in {location}?")

greet_with("siddhart", "delhi")

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
import math
test_h = int(input("Enter the hight of the wall (in mtr.) : "))
test_b = int(input("Enter the breadth of the wall (in mtr.) : "))
test_coverage = int(input("Enter the coverage of the paint (per sqr. mtr) : "))

def cost(hight=test_h, breadth=test_b, coverage=test_coverage):
    no_of_cans = math.ceil((hight*breadth)/coverage)
    print("You need : ",no_of_cans , "cans to paint this wall")

cost()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Prime number checker

n = int(input("Enter the number to check : "))

def prime(n):
    is_prime = True
    for i in range(2,n):
        if n%i == 0 :
            is_prime = False
    if is_prime == True :
        print("The given number is prime.")
    else :
        print("The given number is not prime.")                
prime(n)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ENCODER AND DECODER

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

def encrypt(plain_text, shift_amount):
    sms = ""
    encrypted_text = []
    for i in plain_text:
        x = alphabet.index(i)
        new_position = x + shift_amount
        new_letter = alphabet[new_position]
        encrypted_text.append(new_letter)
    for j in encrypted_text:
        sms += j
    print(sms)    

def decrypt(encoded_text, shift_amount):
    sms = ""
    encrypted_text = []
    for i in encoded_text:
        x = alphabet.index(i)
        new_position = x - shift_amount + 26
        new_letter = alphabet[new_position]
        encrypted_text.append(new_letter)
    for j in encrypted_text:
        sms += j
    print(sms)

if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
elif direction == "decode":
    sms = input("Type message to decode:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(sms, shift) 
else:
    print("Choose the correct option.")

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
