import sys
from django.utils.timezone import now
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()

from django.conf import settings
import uuid


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    id_make = models.CharField(max_length=20, primary_key=True)
    make_name = models.CharField(null=False, max_length=20)
    make_description = models.CharField(max_length=1000)

    def __str__(self):
        return "Make: " + self.make_name + "," + \
             "Description: " + self.make_description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car model object
class CarModel(models.Model):
    model_id = models.CharField(max_length=20, primary_key=True)
    model_name = models.CharField(null=False, max_length=20)
    # Dealer id - refers to id field of dealerships in cloudant
    id = models.IntegerField(null=False, blank=False)
    
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'), 
        (SUV, 'SUV'), 
        (WAGON, 'WAGON')
    ]
    model_type = models.CharField(null=False, max_length=20, choices=TYPE_CHOICES, default=WAGON)
    year = models.DateField(null=False)
    carmake = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    #make = models.ManyToManyField(CarMake)

    def __str__(self):
        return "Model: " + self.model_name + "," + \
            "Type: " + self.model_type
                
# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, id, city, state, st, address, zip, lat, long, short_name, full_name):
        # Dealer id
        self.id = id
        # Dealer city
        self.city = city
        # Dealer state
        self.state = state
        # Dealer state
        self.st = st
        # Dealer address
        self.address = address
        # Dealer zip
        self.zip = zip
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer Full Name
        self.full_name = full_name
        
    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
