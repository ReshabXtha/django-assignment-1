from django.shortcuts import render
from .models import Author, Blog


# Create your views here.
def home(request):
    return render(request, 'index.html')


def blogs(request):
    data = Blog.objects.all()
    context = {
        'data': data
    }

    return render(request, 'blogs.html', context=context)
