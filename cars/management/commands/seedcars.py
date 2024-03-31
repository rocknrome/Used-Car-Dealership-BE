# cars/management/commands/seedcars.py
from django.core.management.base import BaseCommand
from cars.models import Car

class Command(BaseCommand):
    help = 'Seeds the database with cars'

    def handle(self, *args, **kwargs):
        cars = [
    {
        'make': 'Toyota',
        'model': 'Corolla',
        'color': 'Blue',
        'year': 2020,
        'mileage': 15000,
        'price': 20000,
        'description': 'A reliable car',
        'photo': '2020_toyota_corolla_blue_touse.jpg'
    },
    {
        'make': 'Honda',
        'model': 'Civic',
        'color': 'Red',
        'year': 2019,
        'mileage': 10000,
        'price': 18000,
        'description': 'Compact and fuel-efficient',
        'photo': '2019_honda_civic_red_touse.png'
    },
    # Add more cars here (!!!)
]


        for car_data in cars:
            Car.objects.create(**car_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded cars'))
