from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True,)
    def _str_(self):
        return self.name
class Post(models.Model):
    '''данные о записи'''
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100, null=True, blank=True,)
    text = models.TextField(null=True, blank=True,)
    image = models.ImageField(upload_to ='uploads/', height_field=None, width_field=None, max_length=None)
    status = models.BooleanField(null=True, blank=True, default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        default=None
    )
    # categories = models.ManyToManyField(Category, blank=True,)
    def _str_(self):
        return self.title
