from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meeting.models import Meeting

# Create your views here.

def welcome(request):
    return render(request,"website/welcome.html",{"numMeetings":Meeting.objects.count()})

def date(request):
    return HttpResponse("Pagina creada desde: " + str(datetime.now()))

def about(request):
    return HttpResponse("Soy un ingeniero que ha mejorado mucho, debo decirlo, en este camino de progrador,\n me reconzoco eso")
