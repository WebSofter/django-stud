from django.db import models
from django.db.models.signals import pre_save,post_save
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True,)
    class Meta:
        unique_together = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
class Post(models.Model):
    '''данные о записи'''

    # Статусы постов
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # Выборка
    STATUS_CHOICES = (
        (DRAFTED, 'Черновик'),
        (PUBLISHED, 'Опубликован'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    
    slug = models.SlugField(max_length=200, unique=True, editable=False, default=None)
    title = models.CharField(max_length=100, null=True, blank=True,)
    text = models.TextField(null=True, blank=True,)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        related_name='posts',
        verbose_name='Категория'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='uploads/')

    class Meta:
        unique_together = ("title",)
        ordering = ('-date_created',)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'username': self.author.username.lower(), 'slug': self.slug})

    def _str_(self):
        return self.title
