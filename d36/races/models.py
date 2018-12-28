from django.db import models

# Create your models here.
class Event(models.Model):
    """A Distinct Event, ie name of a race"""
    # Contact Info
    name = models.CharField(max_length=25)
    promoter = models.CharField(max_length=25)
   # discipline = models.CharField(choices=['Enduro', 'Cross-Country', 'Flat Track'])

    def __str__(self):
        return self.name + self.promoter
       
class Race(models.Model):
    "A Race event"
    event = models.ForeignKey(Event, on_delete='CASCADE')
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.IntegerField(max_length=9999)
    location = models.CharField(max_length=25)
    rescheduled = models.BooleanField()
    points = models.BooleanField()
    flier_url = models.URLField()

    def __str__(self):
        return self.event.name +str(self.start_date)
