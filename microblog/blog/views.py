from django.shortcuts import render, reverse
from django.contrib.auth import get_user_model

from blog.models import Book, Reader


User = get_user_model()


def index(request):
    context = {}
    return render(request, 'blog/index.html', context=context)


def books_list(request):
    books = Book.objects.order_by('-publication_year', 'title')

    context = {
        'books': books,
    }

    return render(request, 'blog/books.html', context=context)


def readers_list(request):
    readers = Reader.objects.all()

    context = {
        'readers': readers,
    }

    return render(request, 'blog/readers.html', context=context)


def users_list(request):
    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'blog/users.html', context=context)
