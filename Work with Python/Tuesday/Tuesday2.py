my_string = "This is my sting and my name is Hasan"
print("The length of this string is =", len(my_string))

print(50 * '_')

# Using arrays to identify a single letter in strings
print("The letter from the sting", my_string[7])

print(50 * '_')

# i have counted the vaules in the sting and have given a total.
vaule_counterA = my_string.count("a")
vaule_counterE = my_string.count("e")
vaule_counterI = my_string.count("i")
vaule_counterO = my_string.count("o")
vaule_counterU = my_string.count("u")
print("I am counting only the vaules in the string =", vaule_counterA + vaule_counterE + vaule_counterI +
      vaule_counterO + vaule_counterI)

print(50 * '_')

print("this string in upper case looks like ", my_string.upper())

print(50 * '_')

print("This string converted to lower case looks like this = ", my_string.lower())

print(50 * '_')

# this is a new string to play around with.

string_b = "Derrick, Matt, Jessica"
print("string b, however looks like = ", string_b)

print(50 * '_')

# I have split string_b by the commas and put the bits into string_c
string_c = string_b.split(",")
print("If we split string b up by the comma, it becomes three individual elements = ", string_c)
print(string_c[1], "is the 2nd name located in string b, also know as string_c and is type : - "
      , type(string_c), "and has",  len(string_c), "elements")
