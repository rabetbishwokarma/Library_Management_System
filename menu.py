

print("Welcome to Takeo Library Mangement System")  
print(" Choose Menu : ")


menu_number = int(input("Choose Menu Number : 1 For Admin Menu, 2 for Borrower Menu: "))


if menu_number ==1:
    print("Admin Menu : ")
    print(
        
        " Choose 1, to Add a New User,\n"
        " Choose 2,  to Add a new book,\n" 
        " Choose 3,  to Update Book Information,\n"
        " Choose 4,  to Remove a book,\n"
        " Choose 5,  to Remove a User,\n"

        )

elif menu_number == 2:
    print("Borrow Menu")
    print(
        
        " Choose 1 to Lend a Book,\n"
        " Choose 2 to Return a Book,\n" 
        " Choose 3 to Update Personal Information,\n"
        " Choose 4 to Revoke Membership,\n"
    )

