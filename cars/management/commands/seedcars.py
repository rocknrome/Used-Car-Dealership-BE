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
                'photo': 'https://live.staticflickr.com/65535/53623319538_82e45d8d94_m.jpg'
            },
            {
                'make': 'Honda',
                'model': 'Civic',
                'color': 'Red',
                'year': 2019,
                'mileage': 10000,
                'price': 18000,
                'description': 'Compact and fuel-efficient',
                'photo': 'https://live.staticflickr.com/65535/53623560995_0386e3e449_m.jpg'
            },
            # Add more cars here (!!!)
        ]

        for car_data in cars:
            Car.objects.create(**car_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded cars'))
