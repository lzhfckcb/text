# Generated by Django 3.2.5 on 2022-09-20 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_articleviews_viewip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='theme',
        ),
    ]