
class Book():
     def __init__(self,book_id,name,title,author_name,quantity,pub_year,edition):
        self.book_id = book_id
        self.name = name
        self.title = title
        self.author_name  = author_name
        self.quantity = quantity
        self.pub_year = pub_year
        self.edition = edition
        

#CHILD CLASS GETTING ATTRIBUTES FROM PARENT CLASS

class Crime_Thriller_Book(Book):
     def __init__(self,book_id,name,title,author_name,quantity,pub_year,edition,is_part_of_series,crime_thriller_rating):
        super().__init__(self,book_id=book_id,name=name, title=title, author_name=author_name, quantity=quantity, pub_year=pub_year, edition=edition)
        self.is_part_of_series = is_part_of_series
        self.crime_thriller_rating = crime_thriller_rating


class RomanceNovel(Book):
     def __init__(self,book_id,name,title,author_name,quantity,pub_year,edition,is_it_classic):
        super().__init__(self,book_id,name,title,author_name,quantity,pub_year,edition)
        self.is_it_classic = is_it_classic
     
     

     
