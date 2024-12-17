from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.register, name='signup'),
    path('login', views.loginForm, name='login'),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('logout', views.logoutFun, name='logout'),
    path('announcement', views.announcement, name='announcement'),
    path('absence', views.absence, name='absence'),
    path('form_teacher',views.addTeach,name="form_teachers")
]
 
 

