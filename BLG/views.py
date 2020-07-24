from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import AddBlogsForm
from .models import Blog


# Create your views here.
@login_required(login_url='user/login')
def blogs(request):
    data = Blog.objects.all()
    context = {
        'data': data
    }

    return render(request, 'blogs.html', context=context)


@login_required(login_url='user/login')
def add_blog(request):
    if request.method == "POST":
        form = AddBlogsForm(request.POST)
        if form.is_valid():
            b=Blog(
                Title=form.cleaned_data['Title']

            )
    form = AddBlogsForm()
    return render(request, 'addblog.html', {'form': form})
