# Generated by Django 4.2.9 on 2024-05-28 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='content',
            field=models.ManyToManyField(blank=True, related_name='courses', to='content.content'),
        ),
    ]