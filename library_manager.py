import os
import json

LIBRARY_FILE = "library.txt"

# Load library from file if it exists
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            return json.load(f)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)

# Add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").lower()
    read = True if read_input == 'yes' else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the search term: ")

    results = []
    for book in library:
        if choice == "1" and keyword.lower() in book["title"].lower():
            results.append(book)
        elif choice == "2" and keyword.lower() in book["author"].lower():
            results.append(book)

    if results:
        print("Matching Books:")
        for i, book in enumerate(results, start=1):
            print_book(book, i)
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Library is empty.")
        return
    print("Your Library:")
    for i, book in enumerate(library, start=1):
        print_book(book, i)

# Display statistics
def display_stats(library):
    total = len(library)
    if total == 0:
        print("Library is empty.")
        return
    read_books = sum(1 for book in library if book["read"])
    percentage = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%")

# Print a single book
def print_book(book, index):
    status = "Read" if book["read"] else "Unread"
    print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Main menu loop
def menu():
    library = load_library()
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    menu()