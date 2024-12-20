from django.urls import path
from . import views

urlpatterns = [
    path('credits', views.credits, name='home.credits'),
    path('about', views.about, name='home.about'),
    path('version', views.version, name='home.version'),
    path('news', views.news, name = 'home.news'),
]
