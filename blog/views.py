from django.shortcuts import render,get_object_or_404
from .models import Blog


# Create your views here.

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})


def blogDetail(request, blogId):
    blog= get_object_or_404(Blog,pk=blogId)
    return render(request, 'detail.html', {'blog': blog})
