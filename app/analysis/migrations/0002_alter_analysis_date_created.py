# Generated by Django 4.2.9 on 2024-05-23 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
