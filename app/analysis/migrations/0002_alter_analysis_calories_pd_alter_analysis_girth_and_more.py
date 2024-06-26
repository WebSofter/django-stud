# Generated by Django 4.2.9 on 2024-05-29 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='calories_pd',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='girth',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='pulse',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='steps_pd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='weight',
            field=models.FloatField(default=0.0),
        ),
    ]
