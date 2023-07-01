
print("                                         ")
print("Welcome to Takeo Library Management System!")  
print("                                         ")
print("\U0001F4D6 LIBRARY MENU \U0001F4D6 ")
print("                             ")


menu_number = [1,2]
admin_choice = [1,2,3,4,5]
borrower_choice = [1,2,3,4,]


while True:
        menu_number = int(input("1. Admin Menu:\n2. Borrower Menu:\n\nEnter Choice 1/2: "))
        if menu_number not in [1, 2]:
            print("Invalid choice. Please enter 1 or 2.")
        else:
            break

print("                                                               ")


if menu_number ==1:
    print(" Admin Console ")
    print("            ")
    print(
        
        " 1. Add a New User",
        " 2. Remove a User", 
        " 3. Add a Book",
        " 4. Remove a book",
        " 5. Update Book Information",
        sep ="\n"
        )


elif menu_number == 2:
    print("Borrower Console")
    print("            ")
    print(
        
        " 1. Lend a Book\n"
        " 2. Return a Book\n" 
        " 3. Update Personal Information\n"
        " 4. Revoke Membership\n"
        )
    
while True:
    try:
        admin_choice = int(input("Enter Choice 1/5: "))
        if admin_choice in [1, 2, 3, 4, 5]:
            break
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid option.")

        if admin_choice == 1:
                print("New User Dashboard")
                name = input("Name: ")
                email = input("Email: ")
                phone = input("Phone: ")
                address = input("Address: ")
                city = input("City: ")
                zip_code = input("Zip Code: ")
                
        
        print(name, email, phone, address, city, zip_code, sep="\n")





   