from django.shortcuts import render, reverse
from django.contrib.auth import get_user_model

from blog.models import Book, Reader


User = get_user_model()


def index(request):
    context = {
        'nav': {
            'index': reverse('index'),
            'books': reverse('books-list'),
            'readers': reverse('readers-list'),
            'users': reverse('users-list')
        },
        'url': reverse('index')
    }
    return render(request, 'blog/index.html', context=context)


def books_list(request):
    books = Book.objects.order_by('-publication_year', 'title')

    context = {
        'books': books,
        'url': reverse('books-list'),
        'nav': {
            'index': reverse('index'),
            'books': reverse('books-list'),
            'readers': reverse('readers-list'),
            'users': reverse('users-list')
        },
    }

    return render(request, 'blog/books.html', context=context)


def readers_list(request):
    readers = Reader.objects.all()

    context = {
        'readers': readers,
        'url': reverse('readers-list'),
        'nav': {
            'index': reverse('index'),
            'books': reverse('books-list'),
            'readers': reverse('readers-list'),
            'users': reverse('users-list')
        },
    }

    return render(request, 'blog/readers.html', context=context)


def users_list(request):
    users = User.objects.all()

    context = {
        'users': users,
        'url': reverse('users-list'),
        'nav': {
            'index': reverse('index'),
            'books': reverse('books-list'),
            'readers': reverse('readers-list'),
            'users': reverse('users-list')
        },
    }

    return render(request, 'blog/users.html', context=context)
