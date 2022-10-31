
books = {"Margaret Atwood": ["The Handmaiden's Tale" ", " "The Circle Game" ", " "Morning in the Burned House"],
         "J.R.R. Tolkien": ["The Hobbit"], "Roald Dahl": ["Charlie and the Chocolate Factory"]}

print(books["Margaret Atwood"])

print(50 * "_")

for key in books.keys():
    value = books[key]
    print(key, "=", value)

print(50 * "_")

print(sorted(books.values()))

print(50 * "_")

books1 = {"Margaret Atwood": "The Handmaiden's Tale",
         "J.R.R. Tolkien": "The Hobbit",
         "Roald Dahl": "Charlie and the Chocolate Factory"}

print(books1["Margaret Atwood"])

print(sorted(books1.values()))

print(50 * "_")

for values in books1:
    print(values)

