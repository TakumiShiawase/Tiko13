# Generated by Django 4.2.1 on 2023-07-24 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_webpage_settings_display_dob_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage_settings',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
