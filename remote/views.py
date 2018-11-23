from django.shortcuts import render
from django.http import JsonResponse
from data.models import Game, Team, Question, Choice
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

def index(request):
    return render(request, 'remote/index.html')


def buzz(request):
    team_id = request.POST.get('team_id', 0)
    time = datetime.now().timestamp()
    try:
        Team.objects.filter(id=team_id).update(buzz_time=time)
    except ObjectDoesNotExist:
        team_id = 0
    return JsonResponse({
        'datetime': time
    })
