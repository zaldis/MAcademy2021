from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Reader


def readers_list(request):
    readers = Reader.objects.all()

    context = {
        'readers': readers,
    }

    return render(request, 'blog/readers.html', context=context)


class ReaderListView(ListView):
    model = Reader
    template_name = 'blog/readers.html'
    context_object_name = 'readers'