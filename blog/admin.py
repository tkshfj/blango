from django.contrib import admin
from blog.models import Tag, Post, PostAdmin

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
