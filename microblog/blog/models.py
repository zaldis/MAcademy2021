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
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             db_column='book_title',
                             related_name='read_rows',
                             verbose_name='link to book')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             db_column='user_id',
                             related_name='read_rows',
                             verbose_name='link to user')

    class Meta:
        verbose_name = 'reader'
        verbose_name_plural = 'readers'

    def __str__(self):
        return f'Reader <{self.user} reads "{self.book}">'

    def __repr__(self):
        cls_name = type(self).__name__
        return (
            f'{cls_name}(book_title="{self.book}", '
            f'user_id={self.user})'
        )
