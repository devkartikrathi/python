# ODD EVEN CHECKER

x = int(input("Enter the number that you want to check : "))
if x%2 == 0:
    print(x, "is an even number.")
else :
    print(x, "is an odd number.")

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# LEAP YEAR CHECKER

year = int(input("Enter the year you want to check : "))
if year%4 == 0 :
    if year%100 == 0 :
        if year%400 == 0 :
            print("It is a leap year.")
        else :
            print("It is not a leap year.")
    else :
        print("It is a leap year.")
else :
    print("It is not a leap year.")


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#LOVE CALCULATOR

first_name = input("Enter your name?\n")
second_name = input("Enter their name?\n")

x = first_name.lower()
y = second_name.lower()

t1 = x.count("t")
r1 = x.count("r")
u1 = x.count("u")
e1 = x.count("e")
l1 = x.count("l")
o1 = x.count("o")
v1 = x.count("v")
e1 = x.count("e")
t2 = y.count("t")
r2 = y.count("r")
u2 = y.count("u")
e2 = y.count("e")
l2 = y.count("l")
o2 = y.count("o")
v2 = y.count("v")
e2 = y.count("e")

true = t1+r1+u1+e1+t2+r2+u2+e2
love = l1+o1+v1+e1+l2+o2+v2+e2
result = str(true)+str(love)
print(result+"%")

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx