from django.urls import reverse


def routers(request):
    return {
        'routers': {
            'index': reverse('v2:index'),
            'books': reverse('v2:book-list'),
            'readers': reverse('v2:reader-list'),
            'users': reverse('v2:user-list')
        },
        'path': request.path,
    }