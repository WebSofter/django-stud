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
    
    weight = models.FloatField(null=False, blank=False, default=0.0)
    girth = models.FloatField(null=False, blank=False, default=0.0)
    pulse = models.IntegerField(null=False, blank=True, default=0)
    calories_pd = models.IntegerField(null=True, blank=False, default=0)
    steps_pd = models.IntegerField(null=False, blank=False, default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)
    
    def save(self, *args, **kwargs):
        super(Analysis, self).save(*args, **kwargs)

    def _str_(self):
        return self.user.username
