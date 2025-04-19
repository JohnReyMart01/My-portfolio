
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]