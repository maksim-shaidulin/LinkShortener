from django.contrib import admin
from django.urls import path, include
from .views import LinkCreateView, LinksListView, LinkDetailView

app_name = 'link'

urlpatterns = [
    path('create/', LinkCreateView.as_view()),
    path('list/', LinksListView.as_view()),
    path('detail/<int:pk>/', LinkDetailView.as_view()),
]
