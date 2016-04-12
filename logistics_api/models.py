from django.db import models
from django.contrib.auth.models import User
from time import time
from django.forms import ModelForm

# Create your models here.

class Logistics_user(models.Model):
	contact_num = models.IntegerField(default=0, primary_key=True)#check the range of this integer! Also make this a biginteger!
	email_id = models.CharField(max_length=80)
	name = models.CharField(max_length=50)
	password = models.CharField(max_length=30)

	def __unicode__(self):
		return str(self.contact_num)

class Orders(models.Model):
	order_id = models.AutoField(default=0, primary_key = True, auto_created=True)
	goods_type = models.CharField(max_length=30)
	order_status = models.CharField(max_length=10) 
	quantity = models.IntegerField(default=0)
	source = models.CharField(max_length=360)
	destination = models.CharField(max_length=360)
	#date = models.DateTimeField(db_index=True, auto_now_add=True)#take in milliseconds as long. (Use BigInteger field in models)
	contact_num = models.ForeignKey(Logistics_user)
	

	def __unicode__(self):
		return str(self.order_id)

class Truck(models.Model):
	truck_id = models.CharField(max_length=20, primary_key=True)
	truck_capacity = models.IntegerField(default=0)
	truck_status = models.CharField(max_length=20)
	#remaining_capacity = models.IntegerField(default=0)#do we really need this??

	def __unicode__(self):
		return str(self.truck_id)

class Trip(models.Model):
	trip_id = models.IntegerField(default=0, primary_key=True)
	trip_capacity = models.IntegerField(default=0)
	waypoint = models.CharField(max_length=6000) 
	location = models.CharField(max_length=360)
	status = models.CharField(max_length=20)
	order_id = models.ForeignKey(Orders)
	truck_id = models.ForeignKey(Truck)

	def __unicode__(self):
		return str(self.trip_id)

class Driver(models.Model):
	driver_id = models.IntegerField(default=0, primary_key=True)
	name = models.CharField(max_length=30)
	password = models.CharField(max_length=20)
	attendance = models.CharField(max_length=20)
	trip_id = models.ForeignKey(Trip)
