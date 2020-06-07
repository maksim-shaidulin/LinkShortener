from django.shortcuts import render
from .serializers import LinkDetailSerializer, LinkListSerializer
from rest_framework import generics
from .models import Link

class LinkCreateView(generics.CreateAPIView):
    serializer_class = LinkDetailSerializer

class LinksListView(generics.ListCreateAPIView):
    serializer_class = LinkListSerializer
    queryset = Link.objects.all()

class LinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LinkDetailSerializer
    queryset = Link.objects.all()
