# Generated by Django 3.2.5 on 2022-08-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_articleupdown_comment_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.FileField(max_length=128, null=True, upload_to='', verbose_name='头像'),
        ),
    ]
