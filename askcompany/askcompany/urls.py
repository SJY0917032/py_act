from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), # URL Reverse
    path('blog/', include("blog.urls")),
    path('instagram/', include('instagram.urls')),
    path('accounts/', include("accounts.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
# settings.MEDIA_URL
# settings.MEDIA_ROOT
