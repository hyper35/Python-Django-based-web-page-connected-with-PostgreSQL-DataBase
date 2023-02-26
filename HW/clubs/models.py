from django.db import models

# Create your models here.

class Club(models.Model):
	title = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	id = models.AutoField(primary_key=True)

	def __str__(self):
		return self.title


class Event(models.Model):
    Etkinlik_Detay = models.CharField(max_length=255)
    Etkinlik_Sahibi = models.CharField(max_length=255)
    Etkinlik_Tarihi = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Etkinlik_Detay