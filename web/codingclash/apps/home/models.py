import os
import uuid
from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q
from ..teams.models import Team


def _code_save_path(instance, filename):
    print(instance.__dict__)
    return os.path.join(instance.team.name, f"{uuid.uuid4()}.py")


def _replay_save_path(instance, filename):
    return os.path.join("replays", f"{uuid.uuid4()}.txt")


class Submission(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team")
    name = models.CharField(max_length=500, default="")
    submitted_time = models.DateTimeField(auto_now=True)
    code = models.FileField(upload_to=_code_save_path, default=None)

    def get_name(self):
        return self.name

    def get_team_name(self):
        return self.team.name

    def get_submitted_time(self):
        return self.submitted_time.strftime("%Y-%m-%d %H:%M:%S")

    def get_submission_name(self):
        return f'{self.get_name()}: <{self.get_submitted_time()}>'

    def get_code_filename(self):
        return self.code.name

    def delete(self, *args, **kwargs):
        self.code.delete()
        super(Submission, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.get_team_name()}: {self.get_submission_name()}"


class GameSet(models.Manager):
    def get_user_games(self, user):
        return self.get_queryset().filter(Q(red__team__name=user.team.name) |
                                          Q(blue__team__name=user.team.name))

    def get_user_displayable(self, user):
        games = self.get_user_games(user).order_by('timestamp')
        games = [game.get_displayable(user.team) for game in games]
        return games


class Game(models.Model):

    objects = GameSet()

    OUTCOME_CHOICES = (
        ("R", "Red"), ("B", "Blue"), ("T", "Tie")
    )

    red = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name="red")
    blue = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name="blue")
    outcome = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="outcome", blank=True, null=True)
    finished = models.BooleanField(default=False)

    replay = models.FileField(upload_to=_replay_save_path, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def get_red_team(self):
        return self.red.get_team_name()

    def get_blue_team(self):
        return self.blue.get_team_name()

    def get_finished(self):
        return self.finished

    def get_outcome(self):
        return self.outcome

    def get_played_time(self):
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")

    def get_displayable(self, team):
        outcome = "Pending"
        if self.finished:
            if not self.outcome:
                outcome = "Tie"
            elif self.outcome.get_team_name() == team.name:
                outcome = "Won"
            else:
                outcome = "Lost"
        return {
            "red": self.get_red_team(),
            "blue": self.get_blue_team(),
            "outcome": outcome,
            "time": self.get_played_time(),
            "replay": self.replay.url
        }


class GameRequest(models.Model):
    my_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="my_team")
    opp_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="opp_team")


class SubmissionUpload(forms.Form):
    file = forms.FileField()
