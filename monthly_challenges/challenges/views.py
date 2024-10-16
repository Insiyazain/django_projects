from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.

monthly_challenges={
    "january":"Eat no meat for the entire month",
    "february":"walk for atleast 20 minutes every day",
    "march":"Learn django for atleast 20 minutes every day",
    "april":"Eat no meat for the entire month",
    "may":"walk for atleast 20 minutes every day",
    "june":"Learn django for atleast 20 minutes every day"
}

def monthly_challenges_by_number(request, month):
    months=list(monthly_challenges.keys())

    if month>len(months):
        return HttpResponseNotFound("invalid month")
    
    redirect_month= months[month-1]
    return HttpResponseRedirect("/challenges/"+redirect_month)

def monthly_challenge(request,month):
   try:
       challenge_text=monthly_challenges[month]
       return HttpResponse(challenge_text)
   except:
       return HttpResponseNotFound("This month is not supported")