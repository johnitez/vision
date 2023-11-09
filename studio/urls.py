from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('index.html',views.index, name='index'),
    path('about.html',views.about, name='about'),
    
    path('contact.html',views.contact, name='contact'),
    path('gallery.html',views.gallery, name='gallerly'),
    path('main.html',views.main, name='main'),
    path('pricing.html',views.pricing, name='pricing'),
    path('services.html',views.services, name='services'),    
    path('appointment.html',views.appointment, name='appointment'),
    path('video.html',views.video, name='video'),
    path('downloadfile.html',views.downloadfile, name='downloadfile'),
       
]