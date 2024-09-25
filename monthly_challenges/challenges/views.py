from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_text=None
    if month=="january":
        challenge_text="Eat no meat for the entire month!"
    elif month=="february":
        challenge_text="walk for 20 min a day"
    elif month=="March":
        challenge_text="Learn django 20 min a day"
    else:
        return HttpResponseNotFound("This month is not found")
    return HttpResponse(challenge_text)


    return HttpResponse("Walk for atleast 20 minutes every day")