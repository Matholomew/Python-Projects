from django.urls import path
from django.conf.urls import url
from django.conf.urls import handler404, handler500

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('profile/', views.PlayerInfo.as_view(), name='playerInfo'),
    path('tournament/', views.TournamentView.as_view(), name='tournament'),
    path('<int:pk>/tournament/', views.TournamentDetails.as_view(), name='tournamentDetails'),
    path('score/', views.score, name='score'),
    path('newTournament/', views.tournamentCreator, name='newTournament'),
    url(r'^signup/$', views.signup, name='signup'),
]


handler404 = views.error_404
handler500 = views.error_500