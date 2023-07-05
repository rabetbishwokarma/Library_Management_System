import csv
import random


class Borrower:
    def __init__(self, user_name, phone, email, address, city, zip_code, membership_id):
        self.user_name = user_name
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.membership_id = membership_id


    def add_user(self):
        user_data = f"{self.user_name},{self.phone},{self.email},{self.address},{self.city},{self.zip_code},{self.membership_id}\n"
        found = self.search_user_by_membership_id_phone_or_email(self.membership_id, self.email, self.phone)
        if not found:
            with open("user_data.csv", "a+") as file:
                file.write(user_data)
            return True
        else:
            print("User already exists!!!")
            return False

    
    @staticmethod
    def user_exists(user_name, phone, email):
        with open('user_data.csv', 'r+') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) >= 3 and (user_name == row[0] or phone == row[1] or email == row[2]):
                    return True
        return False
    
    
    
    @staticmethod
    def search_user_by_membership_id_phone_or_email(membership_id, email, phone):
        with open("user_data.csv", "r") as file:
            for line in file:
                user_info = line.strip().split(",")
                if len(user_info) >= 7 and user_info[6] == membership_id and user_info[2] == email and user_info[1] == phone:
                    return True
        return False
    



    @staticmethod
    def user_info(membership_id, email, phone):
        with open("user_data.csv", "r") as file:
            for line in file:
                user_info = line.strip().split(",")
                if len(user_info) >= 7 and user_info[6] == membership_id and user_info[2] == email and user_info[1] == phone:
                    print(user_info)
                    print("\n")
                    ask = input("User exists! Do you want to update user information? (yes/no): ")
                    if ask.lower() == "yes":
                        return True
                    else:
                        return False
        return False



    @staticmethod
    def generate_membership_id(user_name):
        membership_id = user_name[:3].upper()+''.join(random.choices('0123456789',k=6))
        return membership_id
    
