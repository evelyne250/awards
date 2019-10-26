from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500)
    name = models.CharField(max_length=120)
    contact = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='pics/')
    design = models.IntegerField(default=0)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project")
    # pub_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.title}'
    def save_project(self):
        self.save()

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
    @classmethod
    def get_all_images(cls):
        images=cls.objects.all().prefetch_related('comment_set')
        return images

class Comment(models.Model):
    posted_by=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    comment_image=models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    comment=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.posted_by
