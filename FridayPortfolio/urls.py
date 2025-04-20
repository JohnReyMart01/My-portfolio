from django.contrib import admin
from django.urls import path, include  # ✅ include must be here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # ✅ no typos
]
