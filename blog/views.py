from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView

from blog.models import Post, Category, Comment, Message,Like
from django.core.paginator import Paginator
from .forms import Contact_us_form , MessageForm
from django.views.generic.base import TemplateView
# Create your views here.


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('comment')
        Comment.objects.create(post=post, body=body, parent_id=parent_id, user=request.user)
    return render(request, 'blog/post_details.html', context={'post': post})


def posts_list(request):
    posts = Post.objects.all()
    posts_has_img = []
    for post in posts:
        if post.img:
            posts_has_img.append(post)
    posts = posts_has_img.copy()
    # page_number = request.GET.get('page')
    # recent_posts = Post.objects.order_by('-create')[:3]
    paginator = Paginator(posts, 1)
    object_list = paginator.get_page(request.GET.get('page'))
    return render(request, "blog/posts_list.html", context={'posts': object_list})


def categories_post(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    posts = category.posts.all()
    return render(request, "blog/posts_list.html", context={'posts': posts})


def search_post(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=query)
    paginator = Paginator(posts, 1)
    object_list = paginator.get_page(request.GET.get('page'))
    return render(request, "blog/posts_list.html", context={'posts': object_list})


def contact_us(request):
    if request.method == 'POST':

        form = MessageForm(data=request.POST)
        if form.is_valid():
            # title = form.cleaned_data['title']
            # text = form.cleaned_data['text']
            # email = form.cleaned_data['email']
            # Message.objects.create(title=title, text=text, email=email)
            #or we can :
            form.save()
            return redirect('home_app:homepage')
    else:
        form = MessageForm()
    return render(request , "blog/contactus.html" , {'form':form})

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data()
            if self.request.user.like.filter(user_id=self.request.user.id , post__slug=self.object.slug).exists():
                context['is_like'] = True
            else:
                context['is_like'] = False
            return context

def like_post(request, slug , pk):

    try:
        like = Like.objects.get(post__slug=slug , user_id=request.user.id)
        like.delete()
        return JsonResponse({"response": "unliked"})
    except:
        Like.objects.create(post_id=pk , user_id=request.user.id)
        return JsonResponse({"response": "liked"})

