import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Racer(models.Model):
    """A District Racer's Profile"""
    # Contact Info
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=12)
    zip_code = models.IntegerField()
    
    # District / AMA Info
    ama_num = models.IntegerField()
    district_num = models.CharField(max_length=5)
    date_joined = models.DateTimeField('date joined')
    
    # Social Media Links
    instragram = models.CharField(max_length=20)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=50)
    
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