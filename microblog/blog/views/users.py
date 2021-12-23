from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import FormView, ListView


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


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 5:
            raise ValidationError('Password must be at least 5 characters')
        return password


class CreateUserView(FormView):
    form_class = CreateUserForm
    template_name = 'blog/create_user.html'

    @property
    def success_path(self):
        return reverse('v2:index')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_path)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect(self.success_path)
        return render(request, self.template_name, {'form': form})
