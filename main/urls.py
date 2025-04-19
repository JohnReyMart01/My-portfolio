from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # Make sure this exists!
    path('contact/', views.contact_view, name='contact'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('project/', views.project, name='project')
]