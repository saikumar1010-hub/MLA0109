# Python Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("\n----- SIMPLE CALCULATOR -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("\nResult:", add(num1, num2))

elif choice == '2':
    print("\nResult:", subtract(num1, num2))

elif choice == '3':
    print("\nResult:", multiply(num1, num2))

elif choice == '4':
    print("\nResult:", divide(num1, num2))

else:
    print("\nInvalid Input!")
