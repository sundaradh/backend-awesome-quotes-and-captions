from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

import category.models as models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'image')
    list_filter = ('id', 'name', 'image')
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
