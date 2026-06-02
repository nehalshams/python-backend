import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from django.db.models import Avg, Sum, Count, Q, OuterRef, Subquery
from home.models import *


# ----------------- Aggragation and Annotation Examples ------------------------

# get total books
def get_total_books():
    count = Book.objects.count()
    print(f"Total number of books: {count}")
    return count


# get total authors
def get_total_authors():
    count = Author.objects.count()
    print(f"Total number of authors: {count}")
    return count

# total sums of book prices
def get_total_book_price():
    total_price = Book.objects.aggregate(total_price = Sum('price'))
    print(f"Total price of all books: {total_price['total_price']}")
    return total_price


# average price of books
def get_average_book_price():
    average_price = Book.objects.aggregate(average_price = Avg('price'))
    print(f"Average price of books: {average_price['average_price']}")
    return average_price


# get count of books with price > 200 
def get_expensive_books(price_threshold = 200):
    expensive_books_count = Book.objects.filter(price__gt=price_threshold).count()
    print(f"Number of books with price greater than {price_threshold}: {expensive_books_count}")
    return expensive_books_count


# total Books written by each author
def get_books_count_by_author():
    books_count = Author.objects.annotate(books_count = Count('book'))
    for author in books_count:
        print(f"Author: {author.name}, Books Count: {author.books_count}")
    return books_count

# average price of books for each author
def get_average_book_price_by_author():
    average_price = Author.objects.annotate(average_price = Avg('book__price'))
    for author in average_price:
        print(f"Author: {author.name}, Average Book Price: {author.average_price}")
    return average_price

# total books punlished in 2023 for each author
def get_books_count_by_author_in_year(year = 2023):
    books_count = Author.objects.annotate(books_count = Count('book', filter=Q(book__published_date__year=year)))
    for author in books_count:
        print(f"Author: {author.name}, Books published in {year}: {author.books_count}")
    return books_count






# ----------------- Subquery Example ------------------------

# Latest book for each author
def get_latest_book_by_author():
    latest_book_subquery = Book.objects.filter(author=OuterRef('id')).order_by('-published_date')
    authors_with_latest_book = Author.objects.annotate(
        latest_book_title=Subquery(latest_book_subquery.values('title')[:1]),
        latest_book_date=Subquery(latest_book_subquery.values('published_date')[:1])
    )
    for author in authors_with_latest_book:
        print(f"Author: {author.name}, Latest Book: {author.latest_book_title}, Published Date: {author.latest_book_date}") 



# total price of book published in 2023 for each author
def get_total_price_of_books_in_years(year = 2021):
    book_price_subquery = Book.objects.filter(
        author = OuterRef('id'),
        published_date__year = year
    ).values('author').annotate(total_price = Sum('price')).values('total_price')

    authors_with_total_price = Author.objects.annotate(
        total_price_in_year = Subquery(book_price_subquery)
    )
    for author in authors_with_total_price:
        print(f"Author: {author.name}, Total Price in {year}: {author.total_price_in_year}")



# count of books published by each author
def get_books_count_by_author():
    books_count_subquery = Book.objects.filter(
        author = OuterRef('id')
    ).values('author').annotate(books_count = Count('id')).values('books_count')

    authors_with_books_count = Author.objects.annotate(
        books_count = Subquery(books_count_subquery)
    )
    for author in authors_with_books_count:
        print(f"Author: {author.name}, Books Count: {author.books_count}")  


# avg price of books published by each author
def get_average_book_price_by_author():
    average_book_price_subquery = Book.objects.filter(
        author = OuterRef('id')
    ).values('author').annotate(average_price = Avg('price')).values('average_price')

    authors_with_average_price = Author.objects.annotate(
        average_price = Subquery(average_book_price_subquery)
    )
    for author in authors_with_average_price:
        print(f"Author: {author.name}, Average Book Price: {author.average_price}")


# most expensive book for each author
def get_most_expensive_book_by_author():
    most_expensive_book_subquery = Book.objects.filter(
        author = OuterRef('id'),
    ).order_by('-price').values('title')[:1]

    authors_with_most_expensive_book = Author.objects.annotate(
        most_expensive_book = Subquery(most_expensive_book_subquery)
    )
    for author in authors_with_most_expensive_book:
        print(f"Author: {author.name}, Most Expensive Book: {author.most_expensive_book}")  


# Authors with atleast one book priced above 300


# Total earnings for each author


# Average price of books published in 2022 for each author


# Authors with books published in each month of 2023



if __name__ == "__main__":
    # get_total_books()
    # get_total_authors()
    # get_total_book_price()
    # get_average_book_price()
    # get_expensive_books(200)

    # get_latest_book_by_author()
    # get_total_price_of_books_in_years(2021)
    get_books_count_by_author()


