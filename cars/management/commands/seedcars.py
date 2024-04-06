from django.core.management.base import BaseCommand
from cars.models import Car
from django.core.files import File
import urllib.request

class Command(BaseCommand):
    help = 'Seeds the database with cars'

    def handle(self, *args, **kwargs):
        cars = [
  {
    "id": 36,
    "photo": null,
    "make": "Toyota",
    "model": "Corolla",
    "color": "Blue",
    "year": 2021,
    "mileage": 15000,
    "price": "20000.00",
    "description": "A reliable everyday commuter",
    "photo_url": "https://live.staticflickr.com/65535/53632512847_071816a4c2.jpg"
  },
  {
    "id": 27,
    "photo": null,
    "make": "Honda",
    "model": "Civic Type R",
    "color": "Yellow",
    "year": 2020,
    "mileage": 26000,
    "price": "27000.00",
    "description": "Got me a wing",
    "photo_url": "https://live.staticflickr.com/65535/53633669323_d06c8c187e.jpg"
  },
  {
    "id": 25,
    "photo": null,
    "make": "Mercedes",
    "model": "AMG GT",
    "color": "Green",
    "year": 2023,
    "mileage": 0,
    "price": "42000.00",
    "description": "Screaming Luxury",
    "photo_url": "https://live.staticflickr.com/65535/53633769204_bbd9c58b7d.jpg"
  },
  {
    "id": 26,
    "photo": null,
    "make": "BMW",
    "model": "M8",
    "color": "Ametrin Metallic",
    "year": 2020,
    "mileage": 1500,
    "price": "37000.00",
    "description": "Bloody beast",
    "photo_url": "https://live.staticflickr.com/65535/53633445186_92a9bbb91d.jpg"
  },
  {
    "id": 43,
    "photo": null,
    "make": "Porsche",
    "model": "911",
    "color": "White",
    "year": 2019,
    "mileage": 70000,
    "price": "50000.00",
    "description": "Wrooom Wroom",
    "photo_url": "https://live.staticflickr.com/65535/53633706438_62befee86d.jpg"
  },
  {
    "id": 33,
    "photo": null,
    "make": "Ford",
    "model": "Mustang Mach 1",
    "color": "Racing Red",
    "year": 2023,
    "mileage": 12000,
    "price": "42000.00",
    "description": "Hot and Fast",
    "photo_url": "https://live.staticflickr.com/65535/53633715908_e3f35020d2.jpg"
  },
  {
    "id": 38,
    "photo": null,
    "make": "Bentley",
    "model": "Continental GT",
    "color": "Moroccan Blue",
    "year": 2024,
    "mileage": 1000,
    "price": "120000.00",
    "description": "Luxury couple",
    "photo_url": "https://live.staticflickr.com/65535/53633745248_068737a91a.jpg"
  },
  {
    "id": 44,
    "photo": null,
    "make": "Ford",
    "model": "Mustang",
    "color": "Dupont Pepper Grey",
    "year": 1967,
    "mileage": 12000,
    "price": "280000.00",
    "description": "Legendary Eleanor",
    "photo_url": "https://live.staticflickr.com/65535/53633823360_f32b8e6497.jpg"
  },
  {
    "id": 34,
    "photo": null,
    "make": "Chevy",
    "model": "Corvette",
    "color": "Sky Blue",
    "year": 2022,
    "mileage": 19000,
    "price": "82000.00",
    "description": "Another one bites the dust",
    "photo_url": "https://live.staticflickr.com/65535/53632524297_d8aa06c44f.jpg"
  },
  {
    "id": 28,
    "photo": null,
    "make": "McLaren",
    "model": "Artura",
    "color": "Indy Orange",
    "year": 2024,
    "mileage": 7000,
    "price": "137000.00",
    "description": "Fast and Furious",
    "photo_url": "https://live.staticflickr.com/65535/53633467416_e0f475d411_z.jpg"
  }
]

        for car_data in cars:
            car = Car.objects.create(
                make=car_data['make'],
                model=car_data['model'],
                color=car_data['color'],
                year=car_data['year'],
                mileage=car_data['mileage'],
                price=car_data['price'],
                description=car_data['description'],
                photo_url=car_data['photo_url']  # Assign the photo_url here
            )
            if 'photo_url' in car_data:
                photo_url = car_data['photo_url']
                # Download the image and save it to the photo field
                response = urllib.request.urlopen(photo_url)
                car.photo.save(f'{car.make}_{car.model}.jpg', File(response), save=True)

        self.stdout.write(self.style.SUCCESS('Successfully seeded cars'))
