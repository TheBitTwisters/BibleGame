from django.shortcuts import render
from django.http import JsonResponse
from data.models import Game, Team, Question, Choice
from django.core.exceptions import ObjectDoesNotExist


def check(request):
    response_game = None
    response_teams = None
    response_question = None
    game = None
    teams = None
    question = None
    choices = None
    try:
        game = Game.objects.get(play=True)
        if game:
            teams = Team.objects.filter(game=game).order_by('-score')
            question = Question.objects.get(game=game.play_question)
            if question:
                choices = Choice.objects.filter(question=question).order_by('-score')
    except ObjectDoesNotExist:
        response_game = None
        response_teams = None
        response_question = None
    if game:
        response_game = { 'id': game.id, 'title': game.title, 'view': game.play_view,
            'question_id': game.play_question, 'time': game.play_time, 'event': game.play_event }
    if teams:
        response_teams = {}
        index = 0
        for team in teams:
            append_team = { 'id': team.id, 'name': team.name, 'score': team.score }
            response_teams[index] = append_team
            index += 1
    if question:
        response_question = { 'id': question.id, 'question_text': question.question_text, 'type': question.type, 'points': question.points, 'choices': {} }
    if choices:
        index = 0
        for choice in choices:
            append_choice = { 'id': choice.id, 'choice_text': choice.choice_text, 'score': choice.score, 'mark': choice.mark }
            response_question['choices'][index] = append_choice
            index += 1
    return JsonResponse({
        'game': response_game,
        'teams': response_teams,
        'question': response_question
    })


def index(request):
    return render(request, 'monitor/index.html')
