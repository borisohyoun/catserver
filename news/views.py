from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news/main.html',  {'posts': posts})
    return render(request, 'news/navbookmark.html',  {'posts': posts})
    return render(request, 'news/navhos.html',  {'posts': posts})
    return render(request, 'news/navmediin.html',  {'posts': posts})
    return render(request, 'news/navmediout.html',  {'posts': posts})
    return render(request, 'news/navmemo.html',  {'posts': posts})
    return render(request, 'news/navweight.html',  {'posts': posts})
# Create your views here.
