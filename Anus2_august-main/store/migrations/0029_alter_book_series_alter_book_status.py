# Generated by Django 4.2.1 on 2023-07-16 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_series_rename_writer_book_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.series'),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('finished', 'Finished'), ('abandoned', 'Abandoned')], default='in_progress', max_length=20),
        ),
    ]
