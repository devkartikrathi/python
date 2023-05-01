# Dictionary

'''traveling =  {
                "key1" : "berlin",
                "key2" : "mosco",
            }

for keys in traveling:
    print(keys)
    print(traveling[keys])'''

'''test = [
        {"ID": 1, "symbol": "ETH", "name": "Etherium"},
        {"ID": 2, "symbol": "SOL", "name": "Solana"},
        {"ID": 3, "symbol": "BTC", "name": "Bitcoin"}
]

x = input("Enter the symbol of the coin : ")

sol = next((coin for coin in test if coin["symbol"]== x), None)
print(sol)'''

# Calculator

def new():

    def add(n1, n2):
        return n1+n2

    def substract(n1, n2):
        return n1-n2

    def multiply(n1, n2):
        return n1*n2

    def divide(n1, n2):
        return n1/n2

    operators = {
        "+" : add,
        "-" : substract,
        "*" : multiply,
        "/" : divide
    }    

    num1 = float(input("Enter the first number : "))

    for symbol in operators:
        print(symbol)
    
    def calculate(num1):
        
        operation_symbol = input("Pick an operator : ")
        num2 = float(input("Enter the next number : ")) 
        calculation_function = operators[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        print("                                  ")
        x = input(f"If you want to continue with {answer} press 'Y', If you want to exit press 'N', If you want to start new calculation press any other key : ")
        print("                                  ")
        if x == "Y" or x == "y":
            num1 = answer
            calculate(num1)
        elif x == "N" or x == "n":
            pass
        else :
            print("START NEW CALCULATION FROM HERE...")
            print("                                  ")
            print("                                  ")
            new()  

    calculate(num1)   

new()