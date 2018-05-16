from django.contrib import admin
from .models import *



class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Categroy)

