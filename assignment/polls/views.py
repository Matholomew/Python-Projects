from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
import datetime
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Tournament, Question
from .models import PlayerInfo as PlayerInfoModel
from .forms import SignUpForm


class TournamentDetails(generic.ListView):
    model = Tournament
    template_name = 'polls/results.html'
    context_object_name = 'Tournament'
    queryset = Tournament.objects.all()

    def get_objects(request):


        return {
               "template_name": "polls/results.html",
               "queryset": Tournament.objects.all(),
               "extra_context" : {"role_list" : Question.objects.all()}
           }

from django.views.generic import TemplateView

class TournamentDetails(TemplateView):
    template_name = 'polls/results.html'

    def get_context_data(self, **kwargs):
         context = super(TournamentDetails, self).get_context_data(**kwargs)
         context['tournaments'] = Tournament.objects.all()
         context['questions'] = Question.objects.all()
         return context


class TournamentView(generic.ListView):
    model = Tournament
    template_name = 'polls/index.html'
    context_object_name = 'Tournament'

    def get_queryset(request):
        return Tournament.objects.all()

class PlayerInfo(generic.ListView):
    model = PlayerInfoModel
    template_name = 'polls/profile.html'
    context_object_name = 'PlayerInfo'

    def get_queryset(request):
        return PlayerInfoModel.objects.all()

class IndexView(generic.ListView):
    model = Tournament
    template_name = 'polls/index.html'
    context_object_name = 'Tournament'

    def get_queryset(request):
        return Tournament.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.all()


def score(request):
   if request.is_ajax():
     if request.method == 'GET':
        pInfo = PlayerInfoModel.objects.get(id=request.GET.get('userid'))
        pInfo.highscore = request.GET.get('total')
        temp = int(pInfo.tournaments_played) + 1
        pInfo.tournaments_played = str(temp)
        pInfo.save()
        return HttpResponse("%s" % pInfo.highscore)



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.


        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



import urllib.request, json

def getJSONData():
    JSONurl = "https://opentdb.com/api.php?amount=10&category=24&difficulty=medium&type=multiple"
    data = ""

    with urllib.request.urlopen(JSONurl) as url:
        data = json.loads(url.read().decode())

    for currentResult in data['results']:
        newQuestion = Question()
        newQuestion.question_text = currentResult['question']
        newQuestion.correct_answer = currentResult['correct_answer']
        incorrectAnswers = []
        for incorrectAnswer in currentResult['incorrect_answers']:
            incorrectAnswers.append(incorrectAnswer)

        newQuestion.incorrect_answers = incorrectAnswers
        newQuestion.category = currentResult['category']
        newQuestion.difficulty = currentResult['difficulty']
        newQuestion.save()

#getJSONData()




def tournamentCreator(request):
   if request.is_ajax():
     if request.method == 'GET':
        tournament = Tournament()
        tournament.tournament_name = request.GET.get('name')
        tournament.category = request.GET.get('category')
        tournament.difficulty = 'Medium'
        tournament.start_date = datetime.datetime.now()
        tournament.end_date = datetime.datetime.now()
        tournament.save()
        return HttpResponse("%s" % tournament.tournament_name )


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/polls/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def error_404(request):
    data = {}
    return render(request, 'polls/error_404.html', data)


def error_500(request):
    data = {}
    return render(request, 'polls/error_500.html', data)