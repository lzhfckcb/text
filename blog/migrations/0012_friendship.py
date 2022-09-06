# Generated by Django 3.2.5 on 2022-08-27 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_userinfo_introduction'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fan', to='blog.userinfo')),
                ('follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to='blog.userinfo')),
            ],
        ),
    ]