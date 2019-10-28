from django.http  import HttpResponse,Http404
import datetime as dt 
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Project, Profile, Comment
from .forms import ProfileForm,ProjectForm,VoteForm, CommentForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import status

# Create your views here.
def welcome(request):
    projects = Project.objects.all()

    return render(request, 'welcome.html',{"projects":projects})

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
	pi_images = Project.objects.filter(user=current_user)

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

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_articles = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def project_review(request,project_id):
  
       single_project = Project.objects.filter(id=project_id).first()
       average_score = round(((single_project.design + single_project.usability + single_project.content)/3),2)
       if request.method == 'POST':
           vote_form = VoteForm(request.POST)
           if vote_form.is_valid():
               single_project.vote_submissions+=1
               if single_project.design == 0:
                   single_project.design = int(request.POST['design'])
               else:
                   single_project.design = (single_project.design + int(request.POST['design']))/2
               if single_project.usability == 0:
                   single_project.usability = int(request.POST['usability'])
               else:
                   single_project.usability = (single_project.usability + int(request.POST['usability']))/2
               if single_project.content == 0:
                   single_project.content = int(request.POST['content'])
               else:
                   single_project.content = (single_project.content + int(request.POST['usability']))/2
               single_project.save()
               return redirect('welcome',project_id)
       else:
           vote_form = VoteForm()

           return render(request,'page.html',{"vote_form":vote_form,"single_project":single_project,"average_score":average_score})

@login_required(login_url='/accounts/login/')     
def add_comment(request,project_id):
    current_user=request.user
    if request.method=='POST':
        image_item=Project.objects.filter(id=project_id).first()

    
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.posted_by=current_user
            comment.comment_image=image_item
            comment.save()
        return redirect('welcome')
    else:
        form=CommentForm()
    return render(request,'comment.html',{"form":form,"project_id":project_id})

class ProfileList(APIView):
    def get(self, request, format=None):
        all_users = Profile.objects.all()
        serializers = ProfileSerializer(all_users, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
