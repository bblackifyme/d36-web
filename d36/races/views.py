from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Event, Race
# Create your views here.

def index(request):
    return HttpResponse("<h1> Hello </h1>")
    
def event(request, event):
	"""View to see a racers details."""
	return HttpResponse("<h1> Hello event</h1>")

def race(request, year, race):
    """View to see a races details."""
    
    return HttpResponse("<h1> Hello %s %s</h1>" % (race, year))