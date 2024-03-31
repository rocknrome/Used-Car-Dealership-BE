from django.contrib import admin
from django.urls import path, include
from cars.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars.urls')),
    path('', home, name='home'),
]
