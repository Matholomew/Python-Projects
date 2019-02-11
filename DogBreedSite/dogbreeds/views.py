from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DogBreed
from .serializers import dogbreedsSerializer

class dogbreedList(APIView):
    def get(self, request):
        dogbreeds1 = DogBreed.objects.all()
        serializer = dogbreedsSerializer(dogbreeds1, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class IndexView(generic.ListView):
    template_name = 'dogbreeds/index.html'
    context_object_name = 'dogbreedObjs'

    def get_queryset(self):
        """Return the last five published dogbreeds."""
        return DogBreed.objects.order_by('-id')

class ResultsView(generic.ListView):
    model = DogBreed
    template_name = 'dogbreeds/results.html'

    def get_queryset(self):
        """Return the last five published dogbreeds."""
        dogbreeds = DogBreed.objects.order_by('-activity')
        output = ', '.join([p.activity for p in dogbreeds])
        return HttpResponse(output)