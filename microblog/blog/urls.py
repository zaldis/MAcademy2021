from django.urls import path, include

from blog import views


urlpatterns = [
    path('v1/', include(
        (
            [
                path('', views.index, name='index'),
                path('books/', views.books_list, name='book-list'),
                path('readers/', views.readers_list, name='reader-list'),
                path('users/', views.users_list, name='user-list'),

                path('500-error/', views.server_death, name='server-death'),
                path('400-error/', views.bad_user_request, name='bad-user-request'),
                path('403-error/', views.permission_denied, name='permission-denied'),
            ],
            'v1',
        ), namespace='v1'
    )),

    path('v2/', include(
        (
            [
                path('', views.IndexView.as_view(), name='index'),
                path('books/', views.BookListView.as_view(), name='book-list'),
                path('books/<title>/', views.BookDetailView.as_view(), name='book-detail'),
                path('books/<title>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
                path('readers/', views.ReaderListView.as_view(), name='reader-list'),
                path('users/', views.UserListView.as_view(), name='user-list')
            ],
            'v2'
        ), namespace='v2'
    )),
]
