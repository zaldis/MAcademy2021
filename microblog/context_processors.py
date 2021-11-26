from django.urls import reverse


def routers(request):
    return {
        'routers': {
            'index': reverse('index'),
            'books': reverse('books-list'),
            'readers': reverse('readers-list'),
            'users': reverse('users-list')
        },
        'path': request.path,
    }