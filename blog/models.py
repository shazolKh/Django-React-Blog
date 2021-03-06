from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    class PostObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter('published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    excerpt = models.TextField(null=True, blank=True)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_post')
    status = models.CharField(max_length=40, choices=options, default='published')
    objects = models.Manager()
    post_object = PostObject()

    class Meta:
        ordering = ('-published', )

    def __str__(self):
        return self.title
