from django.core.management.base import BaseCommand
from cars.models import Car
from django.core.files import File
import urllib.request

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
                'photo_url': 'https://live.staticflickr.com/65535/53623319538_82e45d8d94_m.jpg'
            },
            {
                'make': 'Honda',
                'model': 'Civic',
                'color': 'Red',
                'year': 2019,
                'mileage': 10000,
                'price': 18000,
                'description': 'Compact and fuel-efficient',
                'photo_url': 'https://live.staticflickr.com/65535/53623560995_0386e3e449_m.jpg'
            },
            # Add more cars here (!!!)
        ]

        for car_data in cars:
            car = Car.objects.create(
                make=car_data['make'],
                model=car_data['model'],
                color=car_data['color'],
                year=car_data['year'],
                mileage=car_data['mileage'],
                price=car_data['price'],
                description=car_data['description']
            )
            if 'photo_url' in car_data:
                photo_url = car_data['photo_url']
                # Download the image and save it to the photo field
                response = urllib.request.urlopen(photo_url)
                car.photo.save(f'{car.make}_{car.model}.jpg', File(response), save=True)

        self.stdout.write(self.style.SUCCESS('Successfully seeded cars'))
