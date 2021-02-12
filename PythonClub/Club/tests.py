from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime

# Create your tests here.

class MeetingTest(TestCase):
    def setUp(self):
        self.meeting = Meeting( meetingtitle = 'Code Wars',
                                meetingdate = datetime.date(2021, 2, 20),
                                meetingtime = datetime.time(18, 30),
                                location = 'Warehouse',
                                agenda = 'Hacker triathalon')

    def test_string(self):
        self.assertEqual(str(self.meeting), 'Code Wars')        

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.meetingid = Meeting(meetingtitle = 'Code Wars')
        self.user = User(username = 'user1')
        self.minutes = MeetingMinutes(minutestext = 'TBD')
    
    def test_string(self):
        self.assertEqual(str(self.minutes), 'TBD')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def setUp(self):
        self.resource = Resource(resourcename = 'SCC',
                                 resourcetype = 'school',
                                 resourceurl = 'https://seattlecentral.edu/',
                                 dateentered = datetime.date(2020, 10, 1),
                                 description = 'Local community college with certificate and degree programs')
        self.user = User(username = 'user1')
    
    def test_string(self):
        self.assertEqual(str(self.resource), 'SCC')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.event = Event( eventtitle = 'Spring Registration',
                            location = 'online',
                            eventdate = datetime.date(2021, 3, 1),
                            eventtime = datetime.time(10),
                            description = 'Registration open for enrolled students')
        self.user = User(username = 'user1')
    
    def test_string(self):
        self.assertEqual(str(self.event), 'Spring Registration')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')
