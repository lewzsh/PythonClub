from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import ResourceForm, MeetingForm

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def resources(request):
    resource_list = Resource.objects.all()
    return render(request, 'Club/resources.html', {'resource_list': resource_list})

def meetings(request):
    meetings_list = Meeting.objects.all()
    return render(request, 'Club/meetings.html', {'meetings_list': meetings_list})

def meetingdetails(request, id):
    meetinginfo = get_object_or_404(Meeting, pk=id)
    return render(request, 'Club/meetingdetails.html', {'meetinginfo': meetinginfo})

def newresource(request):
    form = ResourceForm

    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = ResourceForm()
    
    else:
        form = ResourceForm()

    return render(request, 'Club/submitresource.html', {'form' : form})

def newmeeting(request):
    form = MeetingForm

    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()

    return render(request, 'Club/submitmeeting.html', {'form' : form})
