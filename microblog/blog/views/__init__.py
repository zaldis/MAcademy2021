from django.core.exceptions import BadRequest, PermissionDenied

from .books import books_list, BookList
from .index import index
from .readers import readers_list
from .users import users_list


def server_death(request):
    raise Exception


def bad_user_request(request):
    raise BadRequest


def permission_denied(request):
    raise PermissionDenied


__all__ = [
    users_list,
    readers_list,
    books_list, BookList,
    index,

    server_death,
    bad_user_request,
    permission_denied
]
