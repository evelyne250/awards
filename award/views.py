from django.shortcuts import render

# Create your views here.
def welcome(request):
    date = dt.date.today()
    return render(welcome.html,{"date":date})