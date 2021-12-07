from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, CreateView
from django.views.decorators.http import require_http_methods

from blog.models import Book


@require_http_methods(["GET", "POST"])
def books_list(request):
    if request.method == 'GET':
        books = Book.objects.order_by('-publication_year', 'title')
        context = {
            'books': books,
        }
        return render(request, 'blog/books.html', context=context)

    if request.method == 'POST':
        fields = {
            'title': request.POST.get('title'),
            'publication_year': request.POST.get('publication_year')
        }
        Book.objects.create(**fields)

    return HttpResponseRedirect(request.path)


# class BookList(View):

#     def get(self, request, *args, **kwargs):
#         books = Book.objects.order_by('-publication_year', 'title')
#         context = {
#             'books': books,
#         }
#         return render(request, 'blog/books.html', context=context)

#     def post(self, request, *args, **kwargs):
#         fields = {
#             'title': request.POST.get('title'),
#             'publication_year': request.POST.get('publication_year')
#         }
#         Book.objects.create(**fields)
#         return HttpResponseRedirect(request.path)


class BookList(ListView):
    model = Book
    ordering = ['-publication_year', 'title']
    template_name='blog/books.html'
    context_object_name = 'books'

    def post(self, request, *args, **kwargs):
        fields = {
            'title': request.POST.get('title'),
            'publication_year': request.POST.get('publication_year')
        }
        Book.objects.create(**fields)
        return HttpResponseRedirect(request.path)