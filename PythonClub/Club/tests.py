from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import MeetingForm, ResourceForm
from django.urls import reverse

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

class ResourceFormTest(TestCase):
    def test_resourceForm(self):
        data = {'resourcename': 'TestTest',
                'resourcetype': 'website',
                'resourceurl': 'https://google.com',
                'dateentered': '2021-2-22',
                'userid': 'lewis',
                'description': 'Testing if is_valid'}
        form = ResourceForm(data)
        self.assertTrue(form.is_valid)


    #FIXME: this fails to check that an empty form is invalid. 
    # Test description says 'valid=Unknown' so perhaps explicitly stating 
    # parameters that render the form invalid is in order?  

    # def test_resourceForm_empty(self):
    #     data = {}
    #     form = ResourceForm(data)
    #     self.assertFalse(form.is_valid)

class MeetingFormTest(TestCase):
    def test_meetingForm(self):
        data = {'meetingtitle': 'TestMeeting',
                'meetingdate': '2021-2-22',
                'meetingtime': 'noon',
                'location': 'Somewhere nice',
                'agenda': 'Testing if is_valid'}
        form = MeetingForm(data)
        self.assertTrue(form.is_valid)

class MeetingFormAuthTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password = 'P@ssw0rd1')
        self.meeting = Meeting.objects.create( 
                                meetingtitle = 'Code Wars',
                                meetingdate = datetime.date(2021, 2, 20),
                                meetingtime = datetime.time(18, 30),
                                location = 'Warehouse',
                                agenda = 'Hacker triathalon')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('submitmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/submitmeeting/')
    
    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username = 'testuser1', password = 'P@ssw0rd1')
        response = self.client.get(reverse('submitmeeting'))
        
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/submitmeeting.html')


class ResourceFormAuthTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password = 'P@ssw0rd1')
        self.resource = Resource.objects.create(
                                userid = self.test_user,
                                resourcename = 'SCC',
                                resourcetype = 'school',
                                resourceurl = 'https://seattlecentral.edu/',
                                dateentered = datetime.date(2020, 10, 1),
                                description = 'Local community college with certificate and degree programs')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('submitresource'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/submitresource/')
    
    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username = 'testuser1', password = 'P@ssw0rd1')
        response = self.client.get(reverse('submitresource'))
        
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/submitresource.html')