from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Analysis(models.Model):
    '''данные о записи'''
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='analysis',
    )
    
    weight = models.FloatField(null=True, blank=True,)
    girth = models.FloatField(null=True, blank=True,)
    pulse = models.IntegerField(null=True, blank=True,)
    calories_pd = models.IntegerField(null=True, blank=True,)
    steps_pd = models.IntegerField(null=True, blank=True,)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)
    
    def save(self, *args, **kwargs):
        super(Analysis, self).save(*args, **kwargs)

    def _str_(self):
        return self.user.username
