from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, status  # 追加
from rest_framework.response import Response  # 追加
from .models import Live
from .serializers import LiveSerializer


class LiveViewSet(ModelViewSet):
    queryset = Live.objects.all()  # ここが対象となるレコードの指定．今回は全部
    serializer_class = LiveSerializer  # 戻り値を定義したSerializer