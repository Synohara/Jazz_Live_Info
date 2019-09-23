from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Live


class LiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live
        fields = '__all__'


class LiveFilter(filters.FilterSet):
    artist = filters.CharFilter(lookup_expr='contains')
    place = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Live
        fields = ('artist', 'description', 'place')
