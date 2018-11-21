import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Racer(models.Model):
    """A District Racer's Profile"""
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    ama_num = models.IntegerField()
    district_num = models.CharField(max_length=5)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=12)
    zip_code = models.IntegerField()
    date_joined = models.DateTimeField('date joined')
    instragram = models.CharField(max_length=20)
    
    def __str__(self):
    	return ",".join([str(self.ama_num), self.district_num, self.first_name,
    				     self.last_name, self.city, self.state, str(self.date_joined)])

class Sponsors(models.Model):
	"""Sponsors for a given Racer."""
	racer = models.ForeignKey(Racer, on_delete=models.CASCADE)
	sponsor = models.CharField(max_length=25)
	sponsor_img = models.URLField()
	sponsor_url = models.URLField()
	year = models.IntegerField()
	
	def __str__(self):
	    return self.racer.district_num + ":" + self.sponsor
	    
	def is_current(self):
		return self.year >= timezone.now().year