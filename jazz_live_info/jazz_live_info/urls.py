from django.contrib import admin
from django.urls import path, include

from live_info.api_urls import live_router


api_urlpatterns = [
    path('lives/', include(live_router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),
]
