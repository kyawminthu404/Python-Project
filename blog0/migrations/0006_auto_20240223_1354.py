# Generated by Django 2.2 on 2024-02-23 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog0', '0005_auto_20240222_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='auther',
            new_name='author',
        ),
    ]