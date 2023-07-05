import csv
import random

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
        found = self.search_book_by_title_author(self.book_name, self.title, self.author)
        if not found:
            with open('book_data.csv', "a+") as file:
                file.write(book_data)
            return True
        else:
            print(f"Book already exists! 'Title:{self.title}, Author:{self.author}")
            return False

    @staticmethod
    def book_already_exists(book_name, title, author):
        with open('book_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) >= 3 and (book_name == row[0] or title == row[1] or author == row[2]):
                    return True
        return False


    @staticmethod
    def search_book_by_title_author(book_name, title, author,):
        with open('book_data.csv', "r") as file:
            for line in file:
                book_info = line.strip().split(",")
                if len(book_info) >= 3 and book_info[1] == book_name and book_info[1] == title and book_info[2] == author:
                    return True
        return False


    @staticmethod
    def generate_book_id(book_name):
        book_id = book_name[:3].upper()+''.join(random.choices('0123456789',k=6))
        return book_id
    


class Update(Book):
    def __init__(self, book_id, book_name, title, author, quantity, pub_year, edition):
        super().__init__(self, book_id, book_name, title, author, quantity, pub_year, edition)
    Book
