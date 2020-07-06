from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.

def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request, 'Blog/blogHome.html', context)

def blogPost(request, slug):
    Posts = Post.objects.filter(slug=slug).first()
    context = {'Posts':Posts}
    return render(request, 'Blog/blogPost.html', context)