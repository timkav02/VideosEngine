from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.post_search, name='post_search'),
]