from django.http  import HttpResponse
import datetime as dt 
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Project, Profile
from .forms import ProfileForm,ProjectForm
# Create your views here.
def welcome(request):
    date = dt.date.today()
    projects = Project.objects.all()

    return render(request, 'welcome.html',{"date":date,"projects":projects})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('welcome')

    else:
        form = ProjectForm()
    return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request, username=None):
	'''
	Method that fetches a users profile page
	'''
	current_user = request.user
	pi_images = Profile.objects.filter(user=current_user)

	return render(request,"profile.html",locals(),{"pi_images":pi_images})

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user=request.user
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.save()
        return redirect('profile')
    else:
        form=ProfileForm()
    return render(request,'profile_edit.html',{"form":form})
