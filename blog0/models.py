from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class categoryModel(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return self.name


class postModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField(default=None)
    image = models.ImageField(default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(categoryModel, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(default=None)

def _str_(self):
        return self.title

class commentModel(models.Model):
    content = models.TextField(default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    post = models.ForeignKey(postModel, on_delete=models.CASCADE, default=None)

    def _str_(self):
        return self.content

class UserDetailModel(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.TextField()
    phone = models.IntegerField()
    birthday = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def _str_(self):
        return self.address

class CategoryDetailModel(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    category = models.ManyToManyField(categoryModel)
