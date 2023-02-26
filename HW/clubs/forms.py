from django import forms
from django.forms import ModelForm

from .models import *


class ClubForm(forms.ModelForm):
	title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Topluluk Adı yazınız'}))

	class Meta:
		model = Club
		fields = '__all__'


class EventForm(forms.ModelForm):
	Etkinlik_Detay = forms.CharField(widget= forms.TextInput(attrs=
	{'placeholder':'Etkinlik Detayları'}))
	Etkinlik_Sahibi = forms.CharField(widget= forms.TextInput(attrs=
	{'placeholder':'Etkinlik Sahibi Topluluk'}))
	Etkinlik_Tarihi = forms.CharField(widget= forms.TextInput(attrs=
	{'placeholder':'Etkinlik Tarihi Giriniz: GG-AA-YYYY Saat'}))

	class Meta:
		model = Event
		fields = ('Etkinlik_Detay', 'Etkinlik_Sahibi', 'Etkinlik_Tarihi')