from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

from blog.models import Category

class Content(models.Model):
    '''данные о записи'''

    # Тип контента
    RECIPE = "RECIPE"
    IMAGE = "IMAGE"
    FILE = "FILE"
    VIDEO = "VIDEO"
    MENU = "MENU"
    ANALYSIS = "ANALYSIS"
    # Выборка
    TYPE_CHOICES = (
        (RECIPE, 'Рецепт'),
        (IMAGE, 'Изображение'),
        (FILE, 'Файл'),
        (VIDEO, 'Видео'),
        (MENU, 'Меню'),
        (ANALYSIS, 'Анализ'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contents',
    )
    
    slug = models.SlugField(max_length=200, unique=True, editable=False, default=None)
    title = models.CharField(max_length=100, null=True, blank=True)
    text = CKEditor5Field(verbose_name='Текст конента', config_name='extends', null=True, blank=True)
    file = models.FileField(verbose_name='Файл', null=True, blank=True, upload_to='uploads/')
    image = models.ImageField(verbose_name='Фото', null=True, blank=True, default='default.png', upload_to='uploads/')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='RECIPE')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        related_name='contents',
        verbose_name='Категория'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("title",)
        ordering = ('-date_created',)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Content, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('content:content_detail', kwargs={'username': self.author.username.lower(), 'slug': self.slug})

    def _str_(self):
        return self.title
