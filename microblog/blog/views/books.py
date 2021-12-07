from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


class BookListView(ListView):
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


class BookDetailView(DetailView, UpdateView):
    model = Book
    fields = ['title', 'publication_year']
    template_name = 'blog/book_detail.html'
    context_object_name = 'book'

    def get_object(self, queryset=None):
        title = self.kwargs.get('title')
        return get_object_or_404(Book, title=title)


class BookDeleteView(DeleteView):
    model = Book
    
    def get_object(self, queryset=None):
        title = self.kwargs.get('title')
        return get_object_or_404(Book, title=title)

    def get_success_url(self) -> str:
        return reverse('v2:book-list')
