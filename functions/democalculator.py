# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def floor(x,y):
    return x//y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Floor Division")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5'):
        x = float(input("Enter first number: "))
        y= float(input("Enter second number: "))

        if choice == '1':
            print(x, "+", y , "=", add(x,y))

        elif choice == '2':
            print(x , "-", y, "=", subtract(x, y))

        elif choice == '3':
            print(x, "*", y , "=", multiply(x, y))

        elif choice == '4':
            print(x, "/", y, "=", divide(x, y))
        elif choice == '5':
            print(x,"//",y,"=",floor(x,y) )
        break
    else:
        print("Invalid Input")