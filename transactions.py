import csv
from datetime import datetime, timedelta


class Transactions:
    @staticmethod
    def borrow_book(book, borrower, borrow_date, return_date):
        transaction_data = [book.book_name, book.book_id, borrower.membership_id, borrow_date, return_date, "Borrowed"]
        with open('transaction_data.csv', 'a+') as file:
            writer = csv.writer(file)
            writer.writerow(transaction_data)
        book.decrease_quantity()

    @staticmethod
    def return_book(book, borrower):
        with open('transaction_data.csv', 'r') as file:
            rows = list(csv.reader(file))

        with open('transaction_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(rows[0])

            for row in rows[1:]:
                if row[3] == book.book_name and row[2] == borrower.membership_id and row[4] == "Borrowed":
                    row[4] = "Returned"
                    writer.writerow(row)

                    book.decrease_quantity()

    @staticmethod
    def extend_loan(book, borrower):
        return_date = None
        with open('transaction_data.csv', 'r') as file:
            rows = list(csv.reader(file))

        with open('transaction_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(rows[0])

            for row in rows[1:]:
                if row[1] == book.book_id and row[2] == borrower.membership_id and row[5] == "Borrowed":
                    borrow_date = datetime.strptime(row[3], "%Y-%m-%d").date()
                    return_date = borrow_date + timedelta(days=30) + timedelta(days=15)
                    row[4] = return_date.strftime("%Y-%m-%d")
                    writer.writerow(row)

        return return_date
