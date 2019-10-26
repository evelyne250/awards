from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Profile, Project
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(profile_picture  = '/', bio = 'sonOFman', contact='uevelyne44@gmail.com')

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


