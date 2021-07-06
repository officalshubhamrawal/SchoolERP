from django.shortcuts import render,redirect
from school.models import School
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.
def stu_home(request):
	if request.method=="POST":
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get("next"))
			else:
				return redirect('assign')
	else:
		form=AuthenticationForm()

	return render(request,'studhome.html',{'form':form})


@login_required(login_url='stuhome/')
def assign_home(request):
	dorm=School.objects.all()
	return render(request,'assign.html',{'dorm':dorm})

def vote_it(request,poll_id):
	poll=School.objects.get(pk=poll_id)
	if request.method=='POST':
		selected=request.POST['poll']
		if selected=='option1':
			poll.count_ans1+=1
		elif selected=='option2':
			poll.count_ans2+=1
			
		else:
			return HttpResponse(400,'Invalid')
		poll.save()
		messages.success(request, f'Assignment {poll} has been completed.', extra_tags='alert')
		return redirect('assign')
	context={}
	return render(request,'assign.html',context)

	
