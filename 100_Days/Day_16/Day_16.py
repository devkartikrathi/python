class User:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        print("new user being created...")

def inpt():
    name = input("Enter the name of the person to be added : ")
    return(name)

d = {"001" : "kartik"}
x = "003"
d[x] = inpt()
print(d)