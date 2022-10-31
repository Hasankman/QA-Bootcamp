books = {
         "Margaret Atwood": ["The Handmaiden's Tale"  "The Circle Game"  "Morning in the Burned House"],
         "J.R.R. Tolkien": ["The Hobbit", "The Lord of The Rings"],
         "Roald Dahl": ["Charlie and the Chocolate Factory", "The BFG", "The Witches"],
         "George R. R. Martin": ["The Winds Of Winter", "Fire and Blood", "A Game Of Thrones"],
         "Stephenie Meyer": ["New Moon", "Eclipse", "twilight"],
         "Agatha Christie": ["Murder in Mesopotamia", "Murder on the Orient Express"]}


print("List of authors:")
for values in books:
    print(values)

def get_books_by_author(author):
    if author in books:
        book_list = books[author].copy()  # Creates a copy of the author's book list.
        book_list.sort()  # Sorts the list alphabetical order.
        book_string = ", ".join(books[author])
        print(f"The following books are by {author}: {book_string}")
    else:
        print(f"We do not have any books by {author}. Did you enter correctly")


prompt = input("\nPlease enter an author's name: ")
prompt.strip()
get_books_by_author(prompt)
