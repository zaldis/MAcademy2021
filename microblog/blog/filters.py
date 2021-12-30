import django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        # fields = ['title', 'publication_year']
        fields = {
            'title': ['contains'],
            'publication_year': ['exact', 'range', 'gt']
        }