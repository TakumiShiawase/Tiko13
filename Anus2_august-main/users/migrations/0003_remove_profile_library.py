# Generated by Django 4.2.1 on 2023-06-24 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_bookmarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='library',
        ),
    ]
