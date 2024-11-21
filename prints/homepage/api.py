from flask.views import MethodView
from flask import request, abort, jsonify, render_template, redirect, url_for, session,send_from_directory, make_response

from .models import *
import uuid, json, importlib
import json, time
import requests

# response = requests.get(...)
# dictionary = json.loads(response.text)


# # Serializing json  
# json_object = json.dumps(dictionary)


#Time GMT +3
nowtime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(float(time.time()+10800))))



class HomePageAPI(MethodView):

	def get (self):
		return render_template('homepage/index.html')




class ContactUsAPI(MethodView):

	def get (self):
		return render_template('homepage/ContactUs.html')

	def post (self):
		formdata = dict(request.form)
		name, phone, email, message = formdata ['name'], formdata['phone'], formdata['email'], formdata['message']

		formdata["timeOfRegistration"] =time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(float(time.time()))))
		ContactUsTable(**formdata).save()
		return ContactUsTable.objects.all().to_json()
		#return str([name, phone, email, message])




class AboutUsAPI(MethodView):

	def get (self):
		return render_template('homepage/AboutUs.html')



class SlideShowAPI(MethodView):

	def get (self):
		# Specify the directory containing the images
		image_folder = 'static/homepage/slideshowimg'
		
		# Get a list of all jpg files in the directory
		images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg'))]
		
		# Create full URLs for each image
		image_urls = [f"{url_for('static', filename='homepage/slideshowimg/' + img)}" for img in images]



		# Specify the directory containing the videos
		video_folder = 'static/homepage/video'
		
		# Get a list of all video files in the directory
		videos = [f for f in os.listdir(video_folder) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
		
		# Create full URLs for each video
		video_urls = [url_for('static', filename='homepage/video/' + video) for video in videos]
	
		return render_template('homepage/slideshow.html', images=image_urls,  videos=video_urls)
