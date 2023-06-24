from .models import Post
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin


class PostAdmin(ImportExportModelAdmin):
    list_display = ('content', 'author', 'category',
                    'is_active', )
    search_fields = ('content', 'author__username', 'category__name')
    list_filter = ('is_active', 'category__name')
    date_hierarchy = 'date_posted'
    list_per_page = 10
    actions = ('activate', 'deactivate')

    def activate(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(
            request, 'Selected posts have been activated successfully')

    activate.short_description = 'Activate selected posts'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(
            request, 'Selected posts have been deactivated successfully')

    deactivate.short_description = 'Deactivate selected posts'


admin.site.register(Post, PostAdmin)
