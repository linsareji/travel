from django.shortcuts import render
from .models import Places,Team


# Create your views here.
from django.http import HttpResponse


def demo(request):
    obj=Places.objects.all()
    team=Team.objects.all()
   # name="Leena"
    return render(request, "index.html",{'result':obj,'team':team})
    #return HttpResponse("Hellow world")

