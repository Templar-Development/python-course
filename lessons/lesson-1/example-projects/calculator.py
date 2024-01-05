def calculator():
    print("Operation: ")
    print("Add: +")
    print("Subtract: -")
    print("Multiply: x")
    print("Divide: /")
    print("")

    # float allows for decimal numbers (replace with int for whole numbers)
    first_number = float(input("First number: "))
    operation = input("Operation: ")
    second_number = float(input("Second number: "))

    if operation == "+":
        result = add(first_number, second_number)
    elif operation == "-":
        result = subtract(first_number, second_number)
    elif operation == "x":
        result = multiply(first_number, second_number)
    elif operation == "/":
        result = divide(first_number, second_number)
    else:
        print("Invalid operation")
        return
    
    # \n is a newline character
    print("\n")

    # f-string (format string) allows for variables to be inserted into a string
    print(f"Result: {result}")


def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return first_number / second_number


# dont worry about this for now
if __name__ == "__main__":
    calculator()
