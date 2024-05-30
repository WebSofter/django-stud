from django.db import models
from django. contrib.auth.admin import User
from django.dispatch import receiver
from django.db.models.signals import post_save



# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True,)
    class Meta:
        unique_together = ('name',)
        verbose_name = 'role'
        verbose_name_plural = 'roles'

    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    return 'uploads/users/{0}/{1}'.format(instance.user.id, filename)
class Profile(models.Model):
    # Пол
    MALE = "M"
    FEMALE = "F"

    # Выборка
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='profiles',
        verbose_name='Роль'
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Фото', null=True, blank=True, default='userpic.png', upload_to=user_directory_path)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES, default='M')
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    balance = models.FloatField(null=True, blank=True, default=0.0)
    tg_chat = models.CharField(verbose_name='ИД ТГ чата', max_length=100, null=True, blank=True, default=None)
    tg_token = models.CharField(verbose_name='ИД ТГ чата', max_length=150, null=True, blank=True, default=None)

    def _str_(self):
        return self.user.username
    
@receiver (post_save, sender=User)
def create_user_profile (sender, instance, created, **kwargs):
    try:
       if created:
          Profile.objects.create(user=instance).save()
    except Exception as err:
       print(f'Ошибка создания профиля!\n{err}')
    # if created:
    #     Profile.objects.create(user=instance)