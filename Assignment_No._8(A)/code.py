books = [
    {"id": 1, "title": "Dune", "author": "Frank Herbert", "genre": "Science fiction", "status": "Available"},
{"id": 2, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "genre": "Fantasy", "status": "Checked Out"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "status": "Available"},
]

users = [
    {"id": 1, "name": "Ahmad", "borrowed_books": []},
    {"id": 2, "name": "Ali", "borrowed_books": [2]}
]

def view_all_books():
    print("All Books:")
    for book in books:
        print(f"{book['id']}. {book['title']} by {book['author']} ({book['status']})")

def search_book(query):
    print("Search Results:")
    for book in books:
        if query.lower() in book['title'].lower() or query.lower() in book['author'].lower() or query.lower() in book['genre'].lower():
            print(f"{book['id']}. {book['title']} by {book['author']} ({book['status']})")

def borrow_book(user_id, book_id):
    user = next((user for user in users if user['id'] == user_id), None)
    book = next((book for book in books if book['id'] == book_id), None)

    if not user:
        print("User not found.")
        return

    if not book:
        print("Book not found.")
        return

    if book['status'] == "Checked Out":
        print("Book is already checked out.")
        return

    book['status'] = "Checked Out"
    user['borrowed_books'].append(book_id)
    print("Book borrowed successfully.")

def return_book(user_id, book_id):
    user = next((user for user in users if user['id'] == user_id), None)
    book = next((book for book in books if book['id'] == book_id), None)

    if not user:
        print("User not found.")
        return

    if not book:
        print("Book not found.")
        return

    if book['status'] == "Available":
        print("Book is already available.")
        return

    book['status'] = "Available"
    user['borrowed_books'].remove(book_id)
    print("Book returned successfully.")

def view_users():
    print("All Users:")
    for user in users:
        print(f"{user['id']}. {user['name']}")
        for book_id in user['borrowed_books']:
            book = next((book for book in books if book['id'] == book_id), None)
            print(f"  - {book['title']}")

while True:
    print("\nWelcome to the Community Library System!")
    print("----------------------------------------")
    print("Please choose an option:")
    print("1. View all books")
    print("2. Search for a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. View all users")
    print("6. Exit")
    print("----------------------------------------")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        view_all_books()
    elif choice == '2':
        query = input("Enter the search term: ")
        search_book(query)
    elif choice == '3':
        user_id = int(input("Enter your User ID: "))
        book_id = int(input("Enter the Book ID you want to borrow: "))
        borrow_book(user_id, book_id)
    elif choice == '4':
        user_id = int(input("Enter your User ID: "))
        book_id = int(input("Enter the Book ID you want to return: "))
        return_book(user_id, book_id)
    elif choice == '5':
        view_users()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")