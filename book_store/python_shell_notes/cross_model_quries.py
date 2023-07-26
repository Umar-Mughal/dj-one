# Getting All Books where Author's last_name is "Rowling"
books_by_rowling = Book.objects.filter(author__last_name="Rowling")
books_by_rowling
>>> <QuerySet [<Book: Harry Potter 1 (Rating:5)>]>

# Getting All Books where Author's last_name contains "wling"
books_by_rowling = Book.objects.filter(author__last_name__contains="wling")
books_by_rowling
>>> <QuerySet [<Book: Harry Potter 1 (Rating:5)>]>

# INVERSE
# Getting All Author's Books -
# here modelName__set (ex: book_set) is auto defined field  if we do not set ourselves.
jkr = Author.objects.get(first_name="J.K")
jkr
>>> <Author: Author object (1)>
jkr.book_set.all()
<QuerySet [<Book: Harry Potter 1 (Rating:5)>]>

# Getting Author's Data with Custom related_name "books"

from book_outlet.models import Author, Book
jkr = Author.objects.get(first_name="J.K")
jkr.books.all() # ALL BOOKS
>>> <QuerySet [<Book: Harry Potter 1 (Rating:5)>]>
jkr.books.get(title="Harry Potter 1") # SINGLE BOOK
>>> <Book: Harry Potter 1 (Rating:5)>
jkr.books.filter(rating__gt=3) # BOOK WHERE RATING IS GREATER THAN 3
>>> <QuerySet [<Book: Harry Potter 1 (Rating:5)>]>

