from rest_framework import viewsets, permissions
from .models import Car
from .serializers import CarSerializer
from django.http import HttpResponse

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]

    http_method_names = ['get', 'post', 'put', 'delete']

def home(request):
    return HttpResponse("Welcome to the Cars Dealership!")