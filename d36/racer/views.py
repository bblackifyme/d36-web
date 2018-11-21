from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Racer, Sponsors

def index(request):
	racers = Racer.objects.order_by('last_name')
	template = loader.get_template('racer/index.html')
	context = {
		'racers': racers
	}
	return render(request, 'racer/index.html', context)
    
def racer(request, district_num):
	"""View to see a racers details."""
	racer = get_object_or_404(Racer, district_num=district_num)
	try:
		sponsors = Sponsors.objects.filter(racer=racer.id)
	except:
		sponsors = None
	return render(request, 'racer/racer.html', {'racer':racer, 'sponsors':sponsors})
