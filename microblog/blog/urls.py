from django.urls import path

from blog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books_list, name='books-list'),
    path('readers/', views.readers_list, name='readers-list'),
    path('users/', views.users_list, name='users-list'),
]
