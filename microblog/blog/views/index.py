from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    context = {}
    return render(request, 'blog/index.html', context=context)


class IndexView(TemplateView):
    template_name = 'blog/index.html'