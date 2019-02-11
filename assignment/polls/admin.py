from django.contrib import admin

from .models import Tournament, Question, PlayerInfo

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'correct_answer', 'incorrect_answers', 'category', 'difficulty')
    search_fields = ['question_text']

class TournamentAdmin(admin.ModelAdmin):
    list_display = ('tournament_name', 'start_date', 'end_date', 'category', 'difficulty')

class PlayerInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'highscore', 'tournaments_played')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(PlayerInfo, PlayerInfoAdmin)