# a basic calculator using functions and if statments

def add(a, b):
    result = int(a) + int(b)
    return result


def subtract(a, b):
    result = int(a) - int(b)
    return result


def multiply(a, b):
    result = int(a) * int(b)
    return result


def divide(a, b):
    result = int(a) / int(b)
    return result

print("Welcome to your calculator")
print()

a = input("Enter first number:")
method = input("Enter your mathematical operations:")
b = input("Enter second number:")


if method == "+":
    result = add(a, b)
    print(result)
elif method == "-":
    result = subtract(a, b)
    print(result)
elif method == "*":
    result = multiply(a, b)
    print(result)
elif method == "/":
    result = divide(a, b)
    print(result)
else:
    print("please try again")









