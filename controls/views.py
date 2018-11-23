from django.shortcuts import render, redirect
from django.http import JsonResponse
from data.models import Game, Team, Question, Choice
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    games = Game.objects.all()
    game = None
    teams = None
    questions = None
    question = None
    choices = None
    try:
        game = Game.objects.get(play=True)
        teams = Team.objects.filter(game=game)
        questions = Question.objects.filter(game=game)
        choices = Choice.objects.filter(question_id=game.play_question).order_by('-score')
        question = Question.objects.get(id=game.play_question)
    except ObjectDoesNotExist:
        e = ''
    return render(request, 'controls/index.html', {
        'games': games,
        'play_game': game,
        'play_question': question,
        'teams': teams,
        'questions': questions,
        'choices': choices
    })


def home(request):
    return render(request, 'controls/home.html')


def play(request):
    game_id = request.POST.get('game_id', 0)
    try:
        Game.objects.all().update(play=False, play_view='main')
        Game.objects.filter(id=game_id).update(play=True)
    except ObjectDoesNotExist:
        game = None
    return redirect('/controls/')


def view(request):
    view = request.POST.get('view', 'main')
    try:
        game = Game.objects.get(play=True)
        game.play_event = ''
        game.play_view = view
        game.save()
        if view == 'buzzer':
            Team.objects.filter(game=game).update(buzz_time=0)
    except ObjectDoesNotExist:
        game = None
    return redirect('/controls/')


def question(request):
    question_id = request.POST.get('question_id', 0)
    try:
        game = Game.objects.filter(play=True).update(play_question=question_id)
    except ObjectDoesNotExist:
        game = None
    return redirect('/controls/')


def choice(request):
    choice_id = request.POST.get('choice_id', 0)
    try:
        choice = Choice.objects.get(id=choice_id)
        if not choice.mark:
            choice.mark = True
        else:
            choice.mark = False
        choice.save()
    except ObjectDoesNotExist:
        choice = None
    return redirect('/controls/')


def team_score(request):
    team_id = request.POST.get('team_id', 0)
    score = request.POST.get('score', 0)
    try:
        team = Team.objects.get(id=team_id)
        team.score = team.score + int(score)
        team.save()
    except ObjectDoesNotExist:
        team = None
    return redirect('/controls/')


def timer(request):
    time = request.POST.get('time', 0)
    try:
        game = Game.objects.filter(play=True).update(play_time=time)
    except ObjectDoesNotExist:
        game = None
    return redirect('/controls/')


def event(request):
    event = request.POST.get('event', '')
    try:
        game = Game.objects.filter(play=True).update(play_event=event)
    except ObjectDoesNotExist:
        game = None
    return redirect('/controls/')
