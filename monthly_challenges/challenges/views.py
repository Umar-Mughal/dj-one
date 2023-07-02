from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}

# Create your views here.

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(f"{month} challenge: {challenge_text}")
    except:
        return HttpResponse("This month is not supported!")

def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        if month > len(months):
            return HttpResponseNotFound("Invalid Month")
        month = months[month - 1]
        redirect_month_url = reverse("monthly-challenge", args=[month]) # ex: /challenge/january
        return HttpResponseRedirect(redirect_month_url)
    except:
        return HttpResponseNotFound("This month is not supported!")
