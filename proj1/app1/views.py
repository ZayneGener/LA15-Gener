from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello Django')

def say_hi(request):    
    return render(request, 'hi.html', {'name': 'Zayne David Emmanuel M. Gener'})

def blog_list(request):
    post = Post.objects.all()
    context = {
        'blog_list': post
    }
    return render(request, 'blog_list.html', context)

def blog_detail(request, id):
    each_post = get_object_or_404(Post, id=id)
    context = {
        'post': each_post
    }
    return render(request, 'blog_detail.html', context)