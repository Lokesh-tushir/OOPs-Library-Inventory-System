import json
import os

# ==========================================
# MODULE 1: MODELS (Data Blueprints)
# ==========================================

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.times_borrowed = 0  # Analytics feature

    def to_dict(self):
        """Converts object to dictionary for saving to JSON."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_available": self.is_available,
            "times_borrowed": self.times_borrowed
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Book object from a dictionary."""
        book = cls(data["book_id"], data["title"], data["author"])
        book.is_available = data["is_available"]
        book.times_borrowed = data["times_borrowed"]
        return book

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"[ID: {self.book_id}] '{self.title}' by {self.author} ({status})"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # List of Book IDs

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(data["member_id"], data["name"])
        member.borrowed_books = data["borrowed_books"]
        return member

    def __str__(self):
        return f"[ID: {self.member_id}] {self.name} - Books borrowed: {len(self.borrowed_books)}"


# ==========================================
# MODULE 2: LIBRARY MANAGER (Logic & Storage)
# ==========================================

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.data_file = "library_data.json"
        self.load_data() # Load data when library starts

    # --- Book Management ---
    def add_book(self, book_id, title, author):
        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.")
        self.save_data()

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    # --- Member Management ---
    def register_member(self, member_id, name):
        new_member = Member(member_id, name)
        self.members.append(new_member)
        print(f"Member '{name}' registered successfully.")
        self.save_data()

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    # --- Core Functionality ---
    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member and book:
            if book.is_available:
                book.is_available = False
                book.times_borrowed += 1 # Analytics update
                member.borrowed_books.append(book_id)
                print(f"Success! '{book.title}' borrowed by {member.name}.")
                self.save_data()
            else:
                print("Sorry, that book is currently borrowed.")
        else:
            print("Invalid Member ID or Book ID.")

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member and book:
            if book_id in member.borrowed_books:
                book.is_available = True
                member.borrowed_books.remove(book_id)
                print(f"'{book.title}' returned successfully.")
                self.save_data()
            else:
                print("This member does not have this book.")
        else:
            print("Invalid IDs.")

    # --- Analytics Feature ---
    def get_most_borrowed_book(self):
        if not self.books:
            return "No books in library."
        
        # Logic to find the book with highest 'times_borrowed'
        popular_book = max(self.books, key=lambda b: b.times_borrowed)
        
        if popular_book.times_borrowed == 0:
            return "No books have been borrowed yet."
            
        return f"Most Popular: '{popular_book.title}' (Borrowed {popular_book.times_borrowed} times)"

    # --- Data Persistence (Files) ---
    def save_data(self):
        data = {
            "books": [b.to_dict() for b in self.books],
            "members": [m.to_dict() for m in self.members]
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if not os.path.exists(self.data_file):
            return # File doesn't exist yet, start fresh

        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.books = [Book.from_dict(b) for b in data["books"]]
                self.members = [Member.from_dict(m) for m in data["members"]]
            print("Data loaded successfully.")
        except:
            print("Error loading data. Starting fresh.")

# ==========================================
# MODULE 3: MAIN MENU (User Interface)
# ==========================================

def main():
    library = Library()

    while True:
        print("\n--- LIBRARY MENU ---")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Analytics (Most Popular Book)")
        print("6. Show All Books")
        print("7. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            bid = input("Enter Book ID: ")
            title = input("Enter Title: ")
            auth = input("Enter Author: ")
            library.add_book(bid, title, auth)
        elif choice == '2':
            mid = input("Enter Member ID: ")
            name = input("Enter Name: ")
            library.register_member(mid, name)
        elif choice == '3':
            mid = input("Enter Member ID: ")
            bid = input("Enter Book ID: ")
            library.borrow_book(mid, bid)
        elif choice == '4':
            mid = input("Enter Member ID: ")
            bid = input("Enter Book ID: ")
            library.return_book(mid, bid)
        elif choice == '5':
            print(library.get_most_borrowed_book())
        elif choice == '6':
            for book in library.books:
                print(book)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()