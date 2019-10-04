from django.shortcuts import render

def post_list(request):
    return render(request, 'news/main.html', {})
# Create your views here.
