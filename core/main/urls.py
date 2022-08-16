from django.urls import path
from . import views

urlpatterns = [
    path('', views.fibonacci, name='fibonacci'),
    path('res/', views.fib, name='fib'),
    path('about/', views.about, name='about'),


]