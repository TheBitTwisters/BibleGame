from django.contrib import admin
from .models import Game, Question, Choice, Team, Member


# GAME
class GameAdmin(admin.ModelAdmin):
    exclude = ('play', 'play_view', 'play_question', 'play_choice', 'play_time', 'play_refresh', )

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Game, GameAdmin)


# QUESTION & CHOICES
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


# TEAM & MEMBERS
class MemberInline(admin.TabularInline):
    model = Member
    extra = 5

class TeamAdmin(admin.ModelAdmin):
    inlines = [MemberInline]

admin.site.register(Team, TeamAdmin)
