from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Post
from django.urls import reverse


# Create your views here.
def home(request):
    posts = Post.objects.all()
    posts_has_img = []
    for post in posts:
        if post.img :
            posts_has_img.append(post)

    post_recently = posts_has_img[-3:]
    posts_show = posts_has_img[-3:]

    return render(request,
                  'home_app/home.html',
                  {
                      'user': request.user,
                      'posts': posts_has_img,
                      'post_recently': post_recently,
                      'posts_show': posts_show})


# we can use ("django render partial") library for address (more information "https://pypi.org/project/django-render-partial/")


def AboutUs(request):
    return render(request , 'home_app/aboutus.html')