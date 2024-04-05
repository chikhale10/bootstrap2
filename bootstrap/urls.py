from django.contrib import admin
from django.urls import path
from bootstrap import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login.html', views.login, name='login'),
    path('Registration.html', views.Registration, name='Registration'),
    path('ContactUs.html', views.ContactUs, name='ContactUs'),
    path('AboutUs.html', views.AboutUs, name='AboutUs'),

]