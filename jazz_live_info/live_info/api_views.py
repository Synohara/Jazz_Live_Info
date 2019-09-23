from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Live
from .serializers import LiveSerializer, LiveFilter


class LiveViewSet(ModelViewSet):
    queryset = Live.objects.all()
    serializer_class = LiveSerializer

class SearchLiveViewSet(ModelViewSet):
    queryset = Live.objects.all()
    serializer_class = LiveSerializer
    filter_class = LiveFilter