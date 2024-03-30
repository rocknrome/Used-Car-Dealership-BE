from django.contrib import admin
from django.urls import path, include
from cars.views import home  # Adjusted to import 'home' from 'cars.views'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars.urls')),
    path('', home, name='home'),  # Routes the root URL to the 'home' view
]
