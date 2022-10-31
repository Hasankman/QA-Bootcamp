# this is a while loop
names = 0

print(f"type the names of 5 people one at a time")

while names < 5:
    print("type the name of person number", names + 1)
    named_p = input()
    print(named_p, "is awsome!")
    names += 1

print(50 * "_")

# if/else\elif statments (also capitalisation is important and will affect the outcome)

text = "hello world"
print(text.count("o"))

if text.startswith("help"):
    print("its hell in there")
elif text.startswith("help"):
    print("please help me")
else:
    print("Looks like heaven")

# it should be as above

if text.isalpha():
    print("string is all alpha")

# \t = tab \r = carriage return \n = new line... All are blankspaces.. hence "whitespace"
text = "\t\r\n"
if text.isspace():
    print("string is whitespace")
