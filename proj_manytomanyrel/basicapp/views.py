from django.shortcuts import render
from .models import Store, Book

# Create your views here.

def home(request):
    # books = Book.objects.all()   # Run 1 -> n=5 + 1 = 6 queries
    books = Book.objects.all().prefetch_related('store_set')   # Run 2
    # print(books)
    for book in books:
        print(book.store_set.all())  # print all stores for each book obtained from the queryset
    return None

