from rest_framework.routers import DefaultRouter

from . import api_views


live_router = DefaultRouter()
live_router.register(r'', api_views.SearchLiveViewSet)
