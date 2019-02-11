from django.contrib import admin

# Register your models here.

from .models import DogBreed

class DogAdmin(admin.ModelAdmin):
    model = DogBreed
    list_display = ['name', 'activity', 'coat', 'drools', 'goodWC', 'grooming', 'intelligence', 'shedding', 'size', 'image']

admin.site.register(DogBreed, DogAdmin)