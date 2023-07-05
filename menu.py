from books import Book
from borrowers import Borrower

def selection_validate():
    valid_selections = ('1', '2', '3', '4', '5', '6')
    print("                  ") 
    message = input("📖📖📖📖 Welcome to The Library 📖📖📖📖📖 \n\n--------- Press Enter to Continue -------- \n")
 
    loop = 'yes'

    while loop == 'yes':
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
        else:
            if selection in valid_selections:
                loop = 'no'
            else:
                print('\nValue: {} did not match any menu choice'.format(selection))
                loop = 'yes'

    return selection



def selection_calls():
    selection = selection_validate()
    print("          ")

    if selection == '1':
        pass

    elif selection == '2':
       pass
        
       

    elif selection == '3':
        pass
        



    elif selection == '4':
        user_name = input("Enter User Name: ")
        phone = input("Enter Phone number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        zip_code = input("Enter Zip: ")

        membership_id = Borrower.generate_membership_id(user_name)
        user_data = Borrower(user_name, phone, email, address, city, zip_code, membership_id)

        if Borrower.user_exists(user_name, phone, email):
            print("Sorry, user already exists.")
        else:
            result = user_data.add_user()
            if result:
                print(f"User added successfully! Membership ID: {membership_id}")





    elif selection == '5':
        Update_user_info = input("Enter Phone Number :")






    elif selection == '6':

        book_name = input("Enter Book Name: ")
        title = input("Enter Title: ")
        author = input("Enter author: ")
        quantity = input("Enter quantity: ")
        pub_year = input("Enter Publication Year: ")
        edition = input("Enter Edition: ")

        book_id = Book.generate_book_id(book_name)
        new_book = Book(book_id, book_name, title, author, quantity, pub_year, edition)

        if Book.book_already_exists(book_name, title, author):
            print("Sorry, Book already exists!")
        else:
            result = new_book.add_book()
            if result:
                print("Book added successfully, Book Id: {}".format(book_id))
    

if __name__ == '__main__':
    selection_calls()

