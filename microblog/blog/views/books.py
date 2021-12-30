from django import forms
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.core.exceptions import ValidationError
from django.db.models.expressions import F
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.edit import FormView

from blog.models import Book
from blog.filters import BookFilter


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'publication_year', 'photo')
        widgets = {
            'title': forms.TextInput(),
        }

    def clean_publication_year(self):
        publication_year = self.cleaned_data['publication_year']
        if publication_year > timezone.now().year:
            raise ValidationError('You can\'t create the book in the future.')
        return publication_year


class BookDetailForm(BookForm):
    title = forms.CharField(disabled=True)


@require_http_methods(["GET", "POST"])
def books_list(request):
    books = Book.objects.order_by('-publication_year', 'title')
    form = BookForm()
    context = {
        'books': books,
        'form': form
    }

    if request.method == 'GET':
        return render(request, 'blog/books.html', context=context)

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(request.path)

    context['form'] = form
    return render(request, 'blog/books.html', context=context)


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    permission_required = 'blog.add_book'

    def get_success_url(self) -> str:
        created_book = self.get_context_data()['book']
        return reverse('v2:book-detail', args=[created_book.title])


class BookListView(LoginRequiredMixin, ListView, FormView):
    model = Book
    form_class = BookForm
    paginate_by = 5
    ordering = ['-publication_year', 'title']
    template_name='blog/books.html'
    context_object_name = 'books'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        request = self.request

        f = BookFilter(request.GET, self.get_queryset())
        context['filter'] = f

        filter_data = []
        for key, value in f.data.items():
            if key == 'page':
                continue
            filter_data.append(f'{key}={value}')
        filter_str = '&'.join(filter_data)
        context['filter_str'] = filter_str

        return context

    def get_queryset(self):
        request = self.request
        initial_qs = super().get_queryset()
        filtered_qs = BookFilter(request.GET, initial_qs).qs
        return filtered_qs

    def post(self, request, *args, **kwargs):
        books = super().get_queryset()
        view = BookCreateView.as_view(
            extra_context={'books': books},
            template_name=self.template_name
        )
        return view(request, *args, **kwargs)


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    form_class=BookDetailForm
    permission_required = 'blog.change_book'
    template_name = 'blog/book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'title'


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    permission_required = 'blog.delete_book'
    pk_url_kwarg = 'title'

    def get_success_url(self) -> str:
        return reverse('v2:book-list')
