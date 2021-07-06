from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class School(models.Model):
	title=models.CharField(max_length=120)
	question=models.CharField(max_length=120)
	ans1=models.CharField(max_length=30)
	ans2=models.CharField(max_length=30)
	count_ans1=models.IntegerField(default=0)
	count_ans2=models.IntegerField(default=0)
	author=models.ForeignKey(User,blank=True,on_delete=models.CASCADE)


	def __str__(self):
		return self.title
