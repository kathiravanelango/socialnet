from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	# have one to one realtionship with user 
	# on cascade if user is deleted , delete Profile	
	image = models.ImageField(default='default.jpeg',upload_to='profile_pics')
	bio = models.TextField(default='')

	def __str__(self):
		return f'{self.user.username} --> Profile'