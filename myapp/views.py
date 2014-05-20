from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *

# Create your views here.
def update(request,place,direction,statue):
	try:
		p=Places.objects.get(name=place,direction=direction)
		p.crowded = statue
		p.save()
		places = Places.objects.all()
		return HttpResponse('DONE')
	except Exception, e:
		return HttpResponse(e)


def view(request):
	places = Places.objects.all()
	return render(request,
	              'ITS.html',
	              {'places':places})
