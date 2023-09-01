# Generated by Django 4.2.1 on 2023-07-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_alter_book_series_alter_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='abstract',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='book',
            name='author_remark',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='book',
            name='is_adult',
            field=models.BooleanField(default=False),
        ),
    ]