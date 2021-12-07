from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.TextField(primary_key=True, verbose_name="title")
    publication_year = models.PositiveIntegerField(verbose_name="publication year")

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def get_absolute_url(self):
        return reverse("v2:book-detail", kwargs={"title": self.title})

    def __str__(self):
        return f'Book <"{self.title}" in {self.publication_year} year>'

    def __repr__(self):
        cls_name = type(self).__name__
        return (
            f'{cls_name}(title="{self.title}", '
            f'publication_year={self.publication_year})'
        )
