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
                'photo': 'https://ibb.co/ZJ447xL'
            },
            {
                'make': 'Honda',
                'model': 'Civic',
                'color': 'Red',
                'year': 2019,
                'mileage': 10000,
                'price': 18000,
                'description': 'Compact and fuel-efficient',
                'photo': 'https://ibb.co/J281CbZ'
            },
            # Add more cars here (!!!)
        ]

        for car_data in cars:
            Car.objects.create(**car_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded cars'))
