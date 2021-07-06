from .models import School
from django.forms import ModelForm

class CreateForm(ModelForm):
	class Meta:
		model=School
		fields=['title','question','ans1','ans2','author']