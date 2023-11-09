from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Item
from django.http import HttpResponse, HttpRequest
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os


def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')


def contact(request):
	if request.method == 'POST':
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		message_service = request.POST['message-service']
		your_message = request.POST['your-message']
		

		send_mail(
			message_service, # subject
			your_message, # message	
			your_name, # from sender							
			['willylaban@gmail.com'], # To Email
			)

		return render(request, 'contact.html', {
			'your_name': your_name,
			'your_email': your_email,
			'message_service': message_service,
			'your_message': your_message,
			})

	else:
		return render(request, 'contact.html', {})


def gallery(request):
	return render(request, 'gallery.html')

def main(request):
	return render(request, 'main.html')


def pricing(request):
	return render(request, 'pricing.html')


def services(request):
	return render(request, 'services.html')

def appointment(request):
	
	if request.method == 'POST':
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		your_phone = request.POST['your-phone']
		your_time = request.POST['your-time']
		your_date = request.POST['your-date']
		your_service = request.POST['your-service']
		


		# Send an email
		appointment = " Name: " + your_name + "\n" + " Phone: " + your_phone + "\n" + " Email: " + your_email + "\n" + " Date: " + your_date + "\n" + " Time: " + your_time + "\n" + " Service: " +  your_service



		send_mail(
			'Appointment Request', # subject
			appointment, # message
			your_name,	# from email
			['willylaban@gmail.com'], # To Email
			)

		return render(request, 'appointment2.html', {
		   'your_name': your_name,
		   'your_phone': your_phone,
		   'your_email': your_email,
		   'your_date': your_date,
		   'your_time': your_time,
		   'your_service': your_service,		   
			})

	else:
		return render(request, 'appointment.html', {})


def video(request):
	obj=Item.objects.all()
	return render(request, 'video.html', {'obj':obj})

def downloadfile(request):
	base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	filename = 'catalogue2.pdf'
	filepath = base_dir + '/files/' + filename
	thefile = filepath
	filename = os.path.basename(thefile)
	chunk_size = 8192
	response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
		content_type=mimetypes.guess_type(thefile)[0])
	response['Content_Length'] = os.path.getsize(thefile)
	response['Content_Disposition'] = 'Attachment;filrname=%s' % filename
	return response