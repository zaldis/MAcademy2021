from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView


User = get_user_model()


def users_list(request):
    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'blog/users.html', context=context)


class UserListView(ListView):
    model = User
    template_name = 'blog/users.html'
    context_object_name = 'users'