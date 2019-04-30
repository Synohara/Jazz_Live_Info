from django.contrib import admin
from django.urls import path, include  # includeを追加

from live_info.api_urls import live_router  # 定義したquestion_routerをimport


api_urlpatterns = [ 
    path('lives/', include(live_router.urls)),  # 慣例として複数形にする
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),  # api/1.0/としてapi一覧を登録
]
