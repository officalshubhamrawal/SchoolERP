"""schoolit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from school import views as sv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sv.home_page,name="homepage"),
    path('home/', sv.home_view,name="home"),
    path('signup/', sv.signit,name="signup"),
    path('enrol', sv.stulist,name="stulist"),
    path('create/', sv.create_view,name="create"),
    path('logout/', sv.logout_view,name="logout"),
    path('/<title>/',sv.clearit,name="dele"),
    path('student/',include('student.urls')),

]
