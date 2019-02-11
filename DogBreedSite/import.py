import csv,sys,os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DogBreedSite.settings")

import django

django.setup()

from dogbreeds.models import DogBreed

data = csv.reader(open("Dogs.csv"),delimiter=",")

for row in data:
    if row[0] != 'Display Name':
        dogbreed = DogBreed()
        dogbreed.name = row[0]
        dogbreed.activity = row[1]
        dogbreed.coat = row[2]
        dogbreed.drools = row[3]
        dogbreed.goodWC = row[4]
        dogbreed.grooming = row[5]
        dogbreed.intelligence = row[6]
        dogbreed.shedding = row[7]
        dogbreed.size = row[8]
        dogbreed.image = row[9]
        dogbreed.save()