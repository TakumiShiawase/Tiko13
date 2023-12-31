# Generated by Django 4.2.1 on 2023-07-20 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_series_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='author_remark',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='series',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='series',
            name='series_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
