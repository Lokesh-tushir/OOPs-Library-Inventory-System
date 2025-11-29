📚 OOP Library Inventory System
A Python-based command-line application to manage library operations. This project demonstrates core Object-Oriented Programming (OOP) principles, file handling (JSON), and data persistence.

🚀 Features
OOP Design: Built using Book, Member, and Library classes.

Data Persistence: Automatically saves and loads data using a JSON file (library_data.json), so records aren't lost when the program closes.

Inventory Management: Add new books and register new members easily.

Borrowing System: Tracks book availability and assigns books to specific members.

Analytics: Includes a feature to track the "Most Popular Book" based on borrow history.

📂 Project Structure
main.py: Contains the source code for the System, Models, and Menu.

library_data.json: Stores the database of books and members (created automatically).

README.md: Project documentation.

💻 Usage
Clone the repository:

Bash

git clone https://github.com/your-username/oop-library-system.git
Navigate to the directory:

Bash

cd oop-library-system
Run the application:

Bash

python main.py
📸 Demo & Output
Here is an example of the system in action, adding books to the library inventory:

Plaintext

Data loaded successfully.

--- LIBRARY MENU ---
1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. View Analytics (Most Popular Book)
6. Show All Books
7. Exit

Enter choice: 1
Enter Book ID: 012
Enter Title: Haryana
Enter Author: Lokesh Tushir
Book 'Haryana' added successfully.

--- LIBRARY MENU ---
1. Add Book
2. Register Member
3. Borrow Book
...
7. Exit

Enter choice: 1
Enter Book ID: 0000
Enter Title: JAAT
Enter Author: Lokesh Tushir
Book 'JAAT' added successfully.
🛠️ Future Improvements
Add a GUI (Graphical User Interface) using Tkinter.

Add due dates and fine calculation for late returns.

Implement search functionality by Book Title.

👤 Author
Developed by Lokesh Tushir
