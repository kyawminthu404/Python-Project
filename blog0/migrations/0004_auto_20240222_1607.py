# Generated by Django 2.2 on 2024-02-22 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog0', '0003_categorydetailmodel_categorymodel_commentmodel_userdetailmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog0.categoryModel'),
        ),
    ]