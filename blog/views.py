from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
from .models import BlogPost

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('dashboard')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

@login_required
def my_blog_posts(request):
    blog_posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/my_blog_posts.html', {'blog_posts': blog_posts})

def blog_posts_by_category(request, category):
    blog_posts = BlogPost.objects.filter(category=category, draft=False)
    return render(request, 'blog/blog_posts_by_category.html', {'blog_posts': blog_posts, 'category': category})
