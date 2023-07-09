import csv
import random
from books import Book


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
        user_data = [self.user_name, self.phone, self.email, self.address, self.city, self.zip_code, self.membership_id]
        with open("user_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(user_data)
        return True

    @staticmethod
    def user_exists(user_name, phone, email):
        with open('user_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[0] == user_name or row[1] == phone or row[2] == email:
                    return True
        return False

    @staticmethod
    def find_borrower(membership_id):
        with open('user_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[6] == membership_id:
                    user_name = row[0]
                    phone = row[1]
                    email = row[2]
                    address = row[3]
                    city = row[4]
                    zip_code = row[5]
                    return Borrower(user_name, phone, email, address, city, zip_code, membership_id)
        return None

    def has_borrowed_book(self, book_name):
        with open('transaction_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[2] == self.membership_id and row[0] == book_name and row[5] == 'Borrowed':
                    return True
        return False

    def update_user(self, user_name, phone, email, address, city, zip_code):
        with open('user_data.csv', 'r') as file:
            rows = list(csv.reader(file))

        with open('user_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(rows[0])

            for row in rows[1:]:
                if row[6] == self.membership_id:
                    row[0] = user_name if user_name else row[0]
                    row[1] = phone if phone else row[1]
                    row[2] = email if email else row[2]
                    row[3] = address if address else row[3]
                    row[4] = city if city else row[4]
                    row[5] = zip_code if zip_code else row[5]
                writer.writerow(row)

    @staticmethod
    def generate_membership_id(user_name):
        membership_id = user_name[:3].upper() + ''.join(random.choices('0123456789', k=6))
        return membership_id
