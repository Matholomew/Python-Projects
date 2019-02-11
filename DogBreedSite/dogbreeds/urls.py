from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'dogbreeds'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('results/', views.ResultsView.as_view(), name='results'),
    path('api/', views.dogbreedList.as_view(), name='api'),

]