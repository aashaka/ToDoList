from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class toDo(models.Model):
	user=models.ForeignKey(User)
	heading= models.CharField(max_length=100, unique=True)
	description= models.TextField()
	created= models.DateTimeField(auto_now_add=True)
 

	def __str__(self):
		return self.heading


		
	




		



