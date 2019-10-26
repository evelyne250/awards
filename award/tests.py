from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Profile, Project
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(profile_photo  = '/', bio = 'sonOFman', user='Jacl', project='MoringaSacco', first_name='Oruko', last_name ='Clark', phone_number = '0787681304', email = 'pitchclark@gmail.com', created_on = '12-04-2019')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))  

    def test_save_profile(self):
        self.profile.save_profile() 
        profile =Profile.objects.all()
        self.assertTrue(len(profile) > 0) 

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_bio(self):
        self.new_profile.save_profile()
        self.new_profile = Profile.objects.get(id=1)
        profile = self.new_profile
        profile.update_bio('updated user-bio')
        self.updated_profile = Profile.objects.get(id=1)
        self.assertEqual(self.updated_profile.bio,'updated user-bio')


class ProjectTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_profile = UserProfile(user=self.new_user)
        self.new_profile.save()
        self.new_project = Project(id=1,landing_page='photos/photo',project_title='Test Project',project_description='Test Description',user=self.new_user,live_site='http://livesite.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,UserProfile))

    def test_save_project(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_project(self):
        self.new_project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)
                 
