from django.shortcuts import render, HttpResponse,redirect
from time import localtime, strftime
# Create your views here.
def home(request):
    context = {
        "date": strftime(" %A %B %d  %Y", localtime()),
        "time": strftime("%I:%M %p", localtime()),
    }
    return render(request, "home.html", context)