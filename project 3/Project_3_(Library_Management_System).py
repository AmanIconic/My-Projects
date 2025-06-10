import datetime
import json
import os

library_file = "project 3/library_data.json"

def load_data():
    if os.path.exists(library_file):
        with open(library_file, 'r') as f:
            return json.load(f)
    return {"books": {}, "issued": {}}

def save_data(data):
    with open(library_file, 'w') as f:
        json.dump(data, f, indent=4)

def add_book(data):
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    data['books'][book_id] = title
    print(f"Book '{title}' added.")

def remove_book(data):
    book_id = input("Enter book ID to remove: ")
    if book_id in data['books']:
        del data['books'][book_id]
        print("Book removed.")
    else:
        print("Book not found.")

def issue_book(data):
    book_id = input("Enter book ID to issue: ")
    student = input("Enter student name: ")
    if book_id in data['books'] and book_id not in data['issued']:
        issue_date = datetime.date.today()
        due_date = issue_date + datetime.timedelta(days=7)
        data['issued'][book_id] = {
            "student": student,
            "issue_date": str(issue_date),
            "due_date": str(due_date)
        }
        print(f"Book issued to {student}. Due on {due_date}")
    else:
        print("Book not available or already issued.")

def return_book(data):
    book_id = input("Enter book ID to return: ")
    if book_id in data['issued']:
        today = datetime.date.today()
        due_date = datetime.datetime.strptime(data['issued'][book_id]["due_date"], "%Y-%m-%d").date()
        fine = (today - due_date).days * 10 if today > due_date else 0
        print(f"Book returned. Fine: ₹{fine}")
        del data['issued'][book_id]
    else:
        print("Book was not issued.")

def display_books(data):
    print("\nBooks Available:")
    for id, title in data['books'].items():
        status = "Issued" if id in data['issued'] else "Available"
        print(f"{id}: {title} - {status}")

def main():
    data = load_data()
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(data)
        elif choice == '2':
            remove_book(data)
        elif choice == '3':
            issue_book(data)
        elif choice == '4':
            return_book(data)
        elif choice == '5':
            display_books(data)
        elif choice == '6':
            save_data(data)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
