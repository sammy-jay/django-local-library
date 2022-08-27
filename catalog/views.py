from django.shortcuts import render
from django.http import HttpResponse

from .models import BookInstance, Book, Author, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(
        status__exact="a").count()

    num_authors = Author.objects.all().count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "range": [i for i in range(6)]
    }

    return render(request, "catalog/index.html", context=context)
