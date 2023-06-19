import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    print("Welcome to the Scientific Calculator!")

    while True:
        print("Select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("0. Exit")

        choice = input("Enter your choice (0-9): ")

        if choice == "0":
            print("Thank you for using the Scientific Calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid choice! Please try again.")
            continue

        if choice in ["6", "7", "8", "9"]:
            number = get_float_input("Enter a number: ")
        else:
            number1 = get_float_input("Enter the first number: ")
            number2 = get_float_input("Enter the second number: ")

        if choice == "1":
            result = add(number1, number2)
        elif choice == "2":
            result = subtract(number1, number2)
        elif choice == "3":
            result = multiply(number1, number2)
        elif choice == "4":
            if number2 == 0:
                print("Error: Cannot divide by zero!")
                continue
            result = divide(number1, number2)
        elif choice == "5":
            result = power(number1, number2)
        elif choice == "6":
            if number < 0:
                print("Error: Cannot calculate square root of a negative number!")
                continue
            result = sqrt(number)
        elif choice == "7":
            result = sin(number)
        elif choice == "8":
            result = cos(number)
        elif choice == "9":
            result = tan(number)

        print("Result:", result)
        print()

calculator()
