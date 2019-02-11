from rest_framework import serializers
from .models import DogBreed


class dogbreedsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DogBreed;
        fields='__all__'
