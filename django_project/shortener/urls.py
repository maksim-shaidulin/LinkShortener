from django.urls import path

from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<int:link_id>/', views.detail, name='detail'),
]
