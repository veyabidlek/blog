
from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='career'),
    path('statistics', views.stats, name='stats'),
    path('trophies', views.trophies, name='trophies'),
]


