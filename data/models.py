from django.db import models


class Game(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=30, default='SJDV')
    play = models.BooleanField(default=False)
    play_view = models.CharField(max_length=30, default='main')
    play_question = models.IntegerField(default=0)
    play_time = models.IntegerField(default=10)
    play_event = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.date.strftime(' %B %m')


class Question(models.Model):
    QUIZ_TYPE = (
        ('M', 'Multiple Choice'),
        ('T', 'True or False'),
        ('S', 'Survey'),
        ('R', 'Survey Rush'),
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    type = models.CharField(choices=QUIZ_TYPE, max_length=1, default='S')
    question_text = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

    def __str__(self):
        return '[' + str(self.game.id) + self.type + '] ' + self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    mark = models.BooleanField(default=False)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.choice_text


class Team(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    score = models.IntegerField(default=0)

    def __str__(self):
        return '[' + str(self.game.id) + '] ' + self.name


class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return '[' + str(self.team.id) + '] ' + self.name
