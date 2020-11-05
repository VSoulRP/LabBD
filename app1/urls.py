from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app1-home'),
    path('plot/', views.plot, name='app1-plot'),
    path('pais/', views.pais, name='app1-pais'),
    path('dia/', views.dia, name='app1-dia'),
]
