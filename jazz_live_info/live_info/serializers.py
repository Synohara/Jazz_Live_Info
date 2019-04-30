from rest_framework import serializers

from .models import Live


class LiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live
        fields = '__all__'
