# + plus
# - minus
# * multiply
# / division (float)
# // division (integer)
# % reminder

print(5 + 5)
print(10-4)
print(5*5)
print(10/5)
print(12/4)
print(10 % 7)

print(50* "_")

number1 = input("please enter the first number")
option = str(input("please use one og the following methods +, -, / or *:"))
number2 = input("please enter the second number")

if option == "+":
    sum_of = int(number1) + int(number2)
    print(sum_of)
elif option == "-":
    sum_of = int(number1) - int(number2)
    print(sum_of)
elif option == "/":
    sum_of = int(number1) / int(number2)
    print(sum_of)
elif option == "*":
    sum_of = int(number1) * int(number2)
    print(sum_of)
else:
    print("sorry")

