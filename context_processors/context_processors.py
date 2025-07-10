from blog.models import Post, Category


def recent_posts(requeset):
    recent_posts = Post.objects.order_by('-create')[:3]
    return {'recent_posts': recent_posts}

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def posts(request):
    posts = Post.objects.all()
    return {'posts': posts}