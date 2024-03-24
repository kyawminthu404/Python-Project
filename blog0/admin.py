from django.contrib import admin
from blog0.models import postModel,categoryModel,commentModel,UserDetailModel,CategoryDetailModel


# Register your models here.

admin.site.register(postModel)
admin.site.register(categoryModel)
admin.site.register(commentModel)
admin.site.register(UserDetailModel)
admin.site.register(CategoryDetailModel)

