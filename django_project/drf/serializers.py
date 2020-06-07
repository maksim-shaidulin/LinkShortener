from rest_framework import serializers
from .models import Link

class LinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ("short_link", "full_link")

class LinkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"