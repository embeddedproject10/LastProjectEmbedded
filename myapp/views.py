from django.shortcuts import render
from myapp.models import *

# Create your views here.
def update(request,place,direction,statue):
	p=Places.objects.get(name=place,direction=direction)
	p.crowded = statue
	p.save()
	places = Places.objects.all()
	return render(request,
	              'ITS.html',
	              {'places':places})

def view(request):
	places = Places.objects.all()
	return render(request,
	              'ITS.html',
	              {'places':places})

