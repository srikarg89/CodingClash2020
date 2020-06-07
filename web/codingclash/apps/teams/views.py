import json
from django.shortcuts import render

from ..games.models import *



def info(request):
    return render(request, "teams/info.html")


def create_submission(request):
    print(request.FILES)
    for filename, file in request.FILES.items():
        file = request.FILES[filename]
    team = request.user.team
    submission = Submission(team=team, name=file.name, code=file)
    submission.save()


def submission(request):
    if request.method == 'POST':
        form = SubmissionUpload(request.POST, request.FILES)
        print(request.user)
        if form.is_valid():
            create_submission(request)
            return history(request)
    else:
        form = SubmissionUpload()
    return render(request, "teams/submission.html", {'form': form})


def history(request):
#    games = Game.objects.filter(red__user=request.user) | Game.objects.filter(blue__user=request.user)
    games = GameSet.get_user_displayable(request.user)
    print(games)
    return render(request, "teams/history.html", {"games": json.dumps(games)})
