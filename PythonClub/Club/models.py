from django.db import models
from django.contrib.auth.models  import User

# Create your models here.

class Meeting(models.Model):
    meetingtitle = models.CharField(max_length = 255)
    meetingdate = models.DateField()
    meetingtime = models.TimeField()
    location = models.TextField()
    agenda = models.TextField()

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table = 'meeting'

class MeetingMinutes(models.Model):
    meetingid = models.ForeignKey(Meeting, on_delete = models.CASCADE)
    attendance = models.ManyToManyField(User)
    minutestext = models.TextField()

    def __str__(self):
        return self.minutestext

    class  Meta:
        db_table = 'meetingminutes'

class Resource(models.Model):
    resourcename = models.CharField(max_length = 255)
    resourcetype = models.CharField(max_length = 255)
    resourceurl = models.URLField()
    dateentered = models.DateField()
    userid = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    description = models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table = 'resource'

class Event(models.Model):
    eventtitle = models.CharField(max_length = 255)
    location = models.TextField()
    eventdate = models.DateField()
    eventtime = models.TimeField()
    description = models.TextField()
    userid = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table = 'event'