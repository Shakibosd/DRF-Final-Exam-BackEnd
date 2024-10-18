from django.contrib import admin
from .models import Flower, Comment

class FlowerAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'image', 'category', 'stock']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'created_on']

admin.site.register(Flower, FlowerAdmin)
admin.site.register(Comment, CommentAdmin)