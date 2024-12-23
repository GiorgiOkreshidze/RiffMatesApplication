from django.urls import path
from . import views

urlpatterns = [
    path('musician/<int:id>', views.musician, name = 'bands.musician'),
    path('musicians', views.musicians, name = 'bands.musicians'),
    path('band/<int:id>', views.band, name = 'bands.band'),
    path('', views.bands, name = 'bands.bands'),
    path('venues', views.venues, name = 'bands.venues')
]
