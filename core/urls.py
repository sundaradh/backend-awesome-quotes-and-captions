
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Customization of the admin site
admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Awesome Quotes And Captions"

url_patterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('api/', include('category.urls')),
    path('api/', include('post.urls')),
    path('api/', include('notification.urls')),
    path('', admin.site.urls),

]
urlpatterns = static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + url_patterns
