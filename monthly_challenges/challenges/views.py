from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges={
    "january":"Eat no meat for the entire month",
    "february":"walk for atleast 20 minutes every day",
    "march":"Learn django for atleast 20 minutes every day",
    "april":"Eat no meat for the entire month",
    "may":"walk for atleast 20 minutes every day",
    "june":"Learn django for atleast 20 minutes every day"
}

def list_of_challenges(request):
    months=list(monthly_challenges.keys())
    response_form=""

    return render(request,"challenges/index.html",{
        "months":months
    })

    return HttpResponse(response_form)

def monthly_challenges_by_number(request, month):
    months=list(monthly_challenges.keys())

    if month>len(months):
        return HttpResponseNotFound("invalid month")
    
    redirect_month= months[month-1]
    redirect_path=reverse("monthly-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
   try:
       challenge_text=monthly_challenges[month]
       return render(request,"challenges/challenge.html",{
           "text":challenge_text,
           "month_name":month
       })
   except:
       return HttpResponseNotFound("<h2>This month is not supported<h2>")