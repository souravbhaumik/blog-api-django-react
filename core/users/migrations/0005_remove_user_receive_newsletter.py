# Generated by Django 4.0 on 2022-06-30 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_userdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='receive_newsletter',
        ),
    ]
