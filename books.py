import random
import csv


class Book:
    def __init__(self, book_id, book_name, title, author, quantity, pub_year, edition):
        self.book_id = book_id
        self.book_name = book_name
        self.title = title
        self.author = author
        self.quantity = quantity
        self.pub_year = pub_year


        self.edition = edition

    def add_book(self):
        book_data = f"{self.book_name},{self.title},{self.author},{self.quantity},{self.edition},{self.pub_year},{self.book_id}\n"
        if not self.book_already_exists():
            with open('book_data.csv', "a+") as file:
                file.write(book_data)
            return True
        else:
            print(f"Book already exists! Title: {self.title}, Author: {self.author}")
            return False

    def book_already_exists(self):
        with open('book_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) >= 3 and row[0] == self.book_name and row[2] == self.author:
                    return True
        return False

    def is_available(self):
        return int(self.quantity) > 0

    def decrease_quantity(self, amount=1):
        self.quantity = str(max(0, int(self.quantity) - amount))

    @staticmethod
    def search_book_by_title_author(book_name, author):
        with open('book_data.csv', "r") as file:
            for line in file:
                book_info = line.strip().split(",")
                if len(book_info) >= 3 and book_info[0] == book_name and book_info[2] == author:
                    book_id = book_info[6]
                    return Book(book_id, book_name, book_info[1], author, book_info[3], book_info[5], book_info[4])
        return None

    @staticmethod
    def generate_book_id(book_name):
        book_id = book_name[:3].upper() + ''.join(random.choices('0123456789', k=6))
        return ''.join(book_id.split())
