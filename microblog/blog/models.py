from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class Book(models.Model):
    title = models.TextField(primary_key=True, verbose_name="title")
    publication_year = models.PositiveIntegerField(verbose_name="publication year")

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return f'Book <"{self.title}" in {self.publication_year} year>'

    def __repr__(self):
        cls_name = type(self).__name__
        return (
            f'{cls_name}(title="{self.title}", '
            f'publication_year={self.publication_year})'
        )


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name='readers')

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
