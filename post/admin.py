from django.contrib import admin

# Register your models here.
from .models import Content,Post

admin.site.register(Post)
admin.site.register(Content)