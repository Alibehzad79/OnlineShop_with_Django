from django.shortcuts import render


# Create your views here.
from shop_about_us.models import AboutUs, OurTeam


def about_us(request):
    abouts_us = AboutUs.objects.all()
    our_team = OurTeam.objects.all()
    context = {
        "about_us": abouts_us,
        "our_team": our_team
    }
    return render(request, "about_us/about_us.html", context)
