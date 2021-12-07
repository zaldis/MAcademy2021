from django.urls import path, include

from blog import views


urlpatterns = [
    path('v1/', include([
        path('', views.index, name='index'),
        path('books/', views.books_list, name='books-list'),
        path('readers/', views.readers_list, name='readers-list'),
        path('users/', views.users_list, name='users-list'),

        path('500-error/', views.server_death, name='server-death'),
        path('400-error/', views.bad_user_request, name='bad-user-request'),
        path('403-error/', views.permission_denied, name='permission-denied'),
    ])),

    path('v2/', include([
        path('books/', views.BookList.as_view(), name='books_list'),
    ])),
]
