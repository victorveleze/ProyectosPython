from django.shortcuts import render
from .models import Meeting
# Create your views here.

def detail(request, id):
    meeting = meeting.object.get(pk=id)
    return (request, "meeting/detail.html",{"meeting":meeting})