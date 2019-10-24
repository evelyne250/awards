from django.http  import HttpResponse
import datetime as dt
from django.shortcuts import render
# Create your views here.
def welcome(request):
    date = dt.date.today()
    return render(request, 'welcome.html',{"date":date})
