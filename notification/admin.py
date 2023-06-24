from django.contrib import admin

import notification.models as models

#regiseter here


class NotificationAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'message', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'id', 'title', 'message')
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Notification, NotificationAdmin)