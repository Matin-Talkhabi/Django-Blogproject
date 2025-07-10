from django.contrib.auth.models import User
from django.db import models
from django.template.backends import django
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''

class PostManager(models.Manager):
    def counter_post(self):
        return len(self.all())

    def true_status_post(self):
        return len(self.all().filter(status=1))


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ManyToManyField(Category, related_name="posts")
    title = models.CharField(max_length=70)  # unique_for_date='pub_date'
    body = models.TextField()
    img = models.ImageField(upload_to='post/', null=True ,blank=True)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, unique=True)
    objects = models.Manager()
    costume_manager = PostManager()

    # pub_date = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ('-create',)


    def return_img(self):
        if self.img:
            return format_html(f'<img src="{self.img.url}" width="60" height="60" />"')
        return format_html(f'<h3 style="color: #1da0f2">عکس ندارد</h3>')
    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def get_absolute_url(self):
        return reverse('blog:post_data', args=[self.id])

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replay")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() + ' - ' + self.body[:30]



class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    age = models.IntegerField(default=18)
    created = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.title + ' - ' + self.text[:10]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like" )
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name="like")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.post.title}'