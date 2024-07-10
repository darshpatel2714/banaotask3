from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('my_posts/', views.my_blog_posts, name='my_blog_posts'),
    path('<str:category>/', views.blog_posts_by_category, name='blog_posts_by_category'),
]
