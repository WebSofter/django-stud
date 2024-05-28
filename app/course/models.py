from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

from content.models import Category, Content

class Course(models.Model):
    '''курсы'''
    slug = models.SlugField(max_length=200, unique=True, editable=False, default=None)
    title = models.CharField(max_length=100, null=True, blank=True)
    text = CKEditor5Field(verbose_name='Текст конента', config_name='extends', null=True, blank=True)
    image = models.ImageField(verbose_name='Фото', null=True, blank=True, default='default.png', upload_to='uploads/')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        related_name='courses',
        verbose_name='Категория'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses',
    )
    price = models.FloatField(null=True, blank=True, default=0.0)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("title",)
        ordering = ('-date_created',)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Course, self).save(*args, **kwargs)


    def _str_(self):
        return self.title

# class CourseContent(models.Model):
#     '''контент курса'''
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     content = models.ForeignKey(Content, on_delete=models.CASCADE)

# class UserCourseProgress(models.Model):
#     '''прогресс прохождения'''
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     course_content = models.ForeignKey(CourseContent, on_delete=models.CASCADE)
#     is_completed = models.BooleanField(default=False)

# class UserCourseSubscription(models.Model):
#     '''подписка на курсы'''
#     course= models.ForeignKey(Course, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
