# AVERAGE HEIGHT

student_height = input("Enter the heights of the students.\n").split()
for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])
height = 0
students = 0
for i in student_height:
    height += i
    students += 1
average_height = round(height / students)
   
print("The average height of the students is : ",average_height)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# SUM OF ALL EVEN NUMBERS

sum = 0
for i in range(0,101):
    if i % 2 == 0:
        sum += i
    else :
        sum += 0
print(sum)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# GAME

for i in range(0,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0 :
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# PASSWORD MAKER

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter = int(input("Enter the number of 'letters' you want in your password : "))
number = int(input("Enter the number of 'numbers' you want in your password : "))
symbol = int(input("Enter the number of 'symbols you want in your password : "))

# Easy method

password = ""

for char in range(1,letter+1):
    password += random.choice(letters)
for num in range(1,number+1):
    password += random.choice(numbers)
for sym in range(1,symbol+1):
    password += random.choice(symbols)

print (password)

# Hard method

password = [] 

for char in range(1,letter+1):
    password += random.choice(letters)
for num in range(1,number+1):
    password += random.choice(numbers)
for sym in range(1,symbol+1):
    password += random.choice(symbols)

random.shuffle(password)
passwords = ""
for char in password:
    passwords += char

print("Your password is : ",passwords)