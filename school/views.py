from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import School
from .forms import CreateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauth,allowed
from django.contrib.auth.models import Group
# Create your views here.

@unauth
def home_view(request):
	if request.method=="POST":
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get("next"))
			else:
				return redirect('create')
	else:
		form=AuthenticationForm()

	return render(request,'index.html',{'form':form})

@login_required(login_url='home/')
@allowed(allowed_roles=['admin'])
def create_view(request):

	dorm=School.objects.filter(author=request.user)

	if request.method=="POST":
		form=CreateForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Assignment has been created.', extra_tags='alert')
			
	else:
		form=CreateForm()

	return render(request,'create.html',{'form':form,'dorm':dorm})


def logout_view(request):
	if request.method=='POST':
		logout(request)
		return redirect("home")

def clearit(request,title):
	obj = get_object_or_404(School, title = title)
	context={}
	
	if request.method=='POST':
		
		obj.delete()
		return redirect("create")
	return render(request, 'create.html',context)

def home_page(request):
	return render(request,'homepage.html')


def signit(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request, user)
			group= Group.objects.get(name='admin')
			user.groups.add(group)
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request,'signup.html',{'form':form})


@allowed(allowed_roles=['admin'])
def stulist(request):
	dorm=School.objects.all()
	return render(request, 'stulist.html',{'dorm':dorm})

	
		
