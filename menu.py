from books import Book
from borrowers import Borrower
from transactions import Transactions
from datetime import datetime, timedelta


def selection_validate():
    valid_selections = ('1', '2', '3', '4', '5', '6')
    print("                  ")
    input("📖📖📖📖 Welcome to The Library 📖📖📖📖📖 \n\n--------- Press Enter to Continue -------- \n")

    while True:
        selection = input(
            "\n🟢 Please select from the following menu:"
            "\n"
            "\n"
            "🔹 1. To Borrow a Book.\n"
            "🔹 2. To Return a Book.  \n"
            "🔹 3. To Request a loan extension.\n"
            "🔹 4. To Register a New User.\n"
            "🔹 5. To Update User Information. \n"
            "🔹 6. To Add a New Book. \n"
            "🔸 >  To Exit type exit.\n"
            "\n🟢 Enter choice:   "
        )

        if selection == 'exit':
            break

        if selection in valid_selections:
            return selection

        print('\nValue: {} did not match any menu choice'.format(selection))

    return None


def borrow_book():
    membership_id = input("Enter Membership ID: ").upper()
    borrower = Borrower.find_borrower(membership_id)

    if borrower:
        book_name = input("Please enter the name of the book to borrow: ").upper()
        author_name = input("Please enter the author name: ").upper()
        book = Book.search_book_by_title_author(book_name, author_name)

        if book and book.is_available():
            borrow_date = datetime.now().date()
            return_date = borrow_date + timedelta(days=30)
            Transactions.borrow_book(book, borrower, borrow_date, return_date)
            print(f"Book '{book.book_name}' has been successfully borrowed.")
            print(f"Please return the book by {return_date}.")
        elif book and not book.is_available():
            print(f"Book '{book.title}' is already borrowed.")
        else:
            print(f"Book '{book_name}' by '{author_name}' not found.")
    else:
        print("Borrower not found.")



def return_book():
    ask = input("Enter Membership ID: ").upper()
    borrower = Borrower.find_borrower(ask)
    if borrower:
        book_name = input("Please enter the name of the book to return: ").upper()
        author_name = input("Please enter the author name: ").upper()
        book = Book.search_book_by_title_author(book_name, author_name)
        if book:
            if borrower.has_borrowed_book(book_name):
                Transactions.return_book(book=book, borrower=borrower)
                print(f"Book '{book_name}' has been successfully returned.")
            else:
                print(f"Book '{book_name}' has not been borrowed by the member.")
        else:
            print(f"Book '{book_name}' not found.")
    else:
        print("Borrower not found.")



def request_extension():
    ask = input("Enter Membership ID: ").upper()
    borrower = Borrower.find_borrower(ask)
    if borrower:
        book_name = input("Please enter the name of the book: ").upper()
        author_name = input("Please enter the author name: ").upper()
        book = Book.search_book_by_title_author(book_name, author_name)
        if book:
            if borrower.has_borrowed_book(book.book_name):
                return_date = Transactions.extend_loan(book, borrower)
                print(f"Loan extension requested for book '{book_name}'.")
                print(f"Great! New return date for the book is {return_date}. \n Happy Reading!")
            else:
                print(f"Book '{book_name}' has not been borrowed by the member.")
        else:
            print(f"Book '{book_name}' not found.")
    else:
        print("Borrower not found.")



def add_user():
    user_name = input("Enter User Name: ").upper()
    phone = input("Enter Phone number: ")
    email = input("Enter Email: ").upper()
    address = input("Enter Address: ").upper()
    city = input("Enter City: ").upper()
    zip_code = input("Enter Zip: ").upper()

    membership_id = Borrower.generate_membership_id(user_name)
    user_data = Borrower(user_name, phone, email, address, city, zip_code, membership_id)

    if user_data.user_exists(user_name, phone, email):
        print("Sorry, user already exists.")
    else:
        result = user_data.add_user()
        if result:
            print(f"User added successfully! Membership ID: {membership_id}")



def update_user():
    membership_id = input("Enter Membership ID: ").upper()
    borrower = Borrower.find_borrower(membership_id)
    if borrower:
        print(f"User found! Membership ID: {borrower.membership_id}")
        print("Please update the following information (Leave blank to keep current value):")
        user_name = input(f"User Name ({borrower.user_name}): ")
        phone = input(f"Phone number ({borrower.phone}): ")
        email = input(f"Email ({borrower.email}): ")
        address = input(f"Address ({borrower.address}): ")
        city = input(f"City ({borrower.city}): ")
        zip_code = input(f"Zip ({borrower.zip_code}): ")

        borrower.update_user(user_name, phone, email, address, city, zip_code)
        print("User information updated successfully.")
    else:
        print("Borrower not found.")



def add_book():
    book_name = input("Enter Book Name: ").upper()
    title = input("Enter Title: ").upper()
    author = input("Enter author: ").upper()
    quantity = int(input("Enter quantity: "))
    pub_year = input("Enter Publication Year: ")
    edition = input("Enter Edition: ")

    book_id = Book.generate_book_id(book_name)
    new_book = Book(book_id, book_name, title, author, quantity, pub_year, edition)

    if new_book.book_already_exists():
        print("Sorry, Book already exists!")
    else:
        result = new_book.add_book()
        if result:
            print("Book added successfully, Book Id: {}".format(book_id))


def selection_calls():
    selection = selection_validate()
    print("          ")

    if selection == '1':
        borrow_book()
    elif selection == '2':
        return_book()
    elif selection == '3':
        request_extension()
    elif selection == '4':
        add_user()
    elif selection == '5':
        update_user()
    elif selection == '6':
        add_book()


if __name__ == '__main__':
    selection_calls()