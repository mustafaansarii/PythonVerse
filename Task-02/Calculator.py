def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1, 2, 3, or 4): ")

if choice in ('1', '2', '3', '4'):
    if choice == '1':
        result = add(n1, n2)
    elif choice == '2':
        result = subtract(n1, n2)
    elif choice == '3':
        result = multiply(n1, n2)
    elif choice == '4':
        result = divide(n1, n2)
    print(f"Result: {result}")

else:
    print("Invalid choice. Please enter a valid operation (1, 2, 3, or 4).")
