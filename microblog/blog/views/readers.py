from django.shortcuts import render

from blog.models import Reader


def readers_list(request):
    readers = Reader.objects.all()

    context = {
        'readers': readers,
    }

    return render(request, 'blog/readers.html', context=context)