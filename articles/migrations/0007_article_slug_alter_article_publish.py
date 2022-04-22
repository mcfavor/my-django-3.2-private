# Generated by Django 4.0.1 on 2022-04-09 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
