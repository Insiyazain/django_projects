from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

challenges= {
   
   "january":"Eat no meat for the entire month",
   "february":"Walk for atleast 20 min a day",
   "march":"Learn Django for atleast 20 min a day",
   "april":"Eat no meat for the entire month",
   "may":"Walk for atleast 20 min a day",
   "june":"Learn Django for atleast 20 min a day",
   "july":"Eat no meat for the entire month",
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    months=list(challenges.keys())

    if month>len(months):
       return HttpResponseNotFound("Invalid Month")
    redirect_month=months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenges(request, month):
    try:
      challenge_text=challenges[month]
      return HttpResponse(challenge_text)
    except:
       return HttpResponseNotFound("This month is not supported")
  