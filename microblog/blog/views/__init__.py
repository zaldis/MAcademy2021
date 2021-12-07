from django.core.exceptions import BadRequest, PermissionDenied

from .books import books_list, BookListView, BookDetailView, BookDeleteView
from .index import index, IndexView
from .readers import readers_list, ReaderListView
from .users import users_list, UserListView


def server_death(request):
    raise Exception


def bad_user_request(request):
    raise BadRequest


def permission_denied(request):
    raise PermissionDenied


__all__ = [
    users_list, UserListView,
    readers_list, ReaderListView,
    books_list, BookListView, BookDetailView, BookDeleteView,
    index, IndexView,

    server_death,
    bad_user_request,
    permission_denied
]
