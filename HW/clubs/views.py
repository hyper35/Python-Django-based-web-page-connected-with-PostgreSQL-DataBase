from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.

def index(request):
	clubs = Club.objects.all()

	form = ClubForm()

	if request.method =='POST':
		form = ClubForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	return render(request, 'clubs/list.html', {'clubs':clubs, 'form':form})


def updateClub(request, pk):
	club = Club.objects.get(id=pk)
	form = ClubForm(instance=club)

	if request.method == 'POST':
		form = ClubForm(request.POST, instance=club)
		if form.is_valid():
			form.save()
			return redirect('/')

	return render(request, 'clubs/update_club.html', {'form':form})


def deleteClub(request, pk):
	item = Club.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	return render(request, 'clubs/delete_club.html', {'item':item})


def table_view(request):
	form = EventForm()
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('table')

	else:
		form = EventForm()
	inputs = Event.objects.all()
	return render(request, 'clubs/table.html', {'form': form, 'inputs': inputs})


def update_event(request, pk):
	event = Event.objects.get(id=pk)
	form = EventForm(instance=event)

	if request.method == 'POST':
		form = EventForm(request.POST, instance=event)
		if form.is_valid():
			form.save()
			return redirect('table')

	return render(request, 'clubs/update_event.html', {'form':form})

def delete_event(request, pk):
	item = Event.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('table')

	return render(request, 'clubs/delete_event.html', {'item':item})