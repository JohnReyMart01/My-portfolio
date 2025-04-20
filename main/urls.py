from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('project/', views.project, name='project'),
    path('hobbies/', views.hobbies, name='hobbies'),
]
