# Generated by Django 3.0.8 on 2020-08-06 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200804_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='header_image',
        ),
    ]
