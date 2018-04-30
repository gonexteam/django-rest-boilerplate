from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from v1.apps.accounts.routes import router


urlpatterns = [
    # CORE
    path('admin/', admin.site.urls),

    # API (v1)
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='api_auth'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
