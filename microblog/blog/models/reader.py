from django.contrib.auth import get_user_model
from django.db import models

from .book import Book


User = get_user_model()


class ReaderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('user').prefetch_related('books')


class Reader(models.Model):
    user = models.OneToOneField(User, related_name='reader', db_column=..., on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name='readers')

    objects = ReaderManager()

    class Meta:
        verbose_name = 'reader'
        verbose_name_plural = 'readers'

    def __str__(self):
        return (
            f'Reader <{self.user} reads "{self.books.count()} books">'
        )

    def __repr__(self):
        cls_name = type(self).__name__
        books = [book for book in self.books.all()]
        return (
            f'{cls_name}(books="{books}", '
            f'user_id={self.user_id})'
        )