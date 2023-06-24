from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

import post.models as models


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'content',
        'image',
        'date_posted',
        'author',
        'category',
        'total_likes'
    )
    list_filter = (
        'date_posted',
        'author',
        'category',
        'id',
        'content',
        'image',
    )
    fields = [
        'content',
        'image',
        'author',
        'category',
        'likes',
    ]
    readonly_fields = [
        'total_likes',
    ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Post, PostAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'post',
    )
    list_filter = (
        'id',
        'user',
        'post',
    )


_register(models.Like, LikeAdmin)


class FavoriteAdmin(admin.ModelAdmin):
    pass


_register(models.Favorite, FavoriteAdmin)
