from unicodedata import category
from django.db import models
from django.utils import timezone

from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    status_options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250, blank=True, null=True)
    excerpt = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='blog_posts', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=status_options, default='published', blank=True, null=True)

    objects = models.Manager()      # Default Manager
    postobjects = PostObjects()     # Custom Manager

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title
