from django.db import models
from datetime import datetime
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address!"
        users_with_email = User.objects.filter(email = postData['email'])
        if len(users_with_email) >= 1:
            errors['duplicate'] = "Email already exists."
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['pw_match'] = "Password must match!"
        return errors

class TripManager(models.Manager):
    def trip_validator(self,postData):
        errors = {}
        if len(postData['dest']) < 3:
            errors['dest'] = "Destination must be at least 3 characters"
        if postData ['start_date'] ==  "":
            errors['start_date'] = "Please enter a Start Date"
        elif datetime.strptime(postData['start_date'], '%Y-%m-%d') < datetime.now():
            errors['start_date'] = "Start Date should be in the future"
        if postData ['end_date'] ==  "":
            errors['end_date'] = "Please enter a End Date"
        elif datetime.strptime(postData['start_date'], '%Y-%m-%d') > datetime.strptime(postData['end_date'], '%Y-%m-%d'):
            errors['end_date'] = 'End Date should be after the Start Date'
        
        # if datetime.datetime(postData['start_date'], '%Y-%m-%d') < datetime.now():
        #     errors['start_date'] = "Please enter Start Date"
        # if datetime.strptime(postData['end_date'], '%Y-%m-%d') < datetime.now():
        #     errors['end_date'] = "Please enter End Date"
        # if datetime.strptime(postData['start_date'], '%Y-%m-%d') < datetime.now():
        #     errors['start_date'] = "Start Date should be in the future"
        # if datetime.strptime(postData['start_date'], '%Y-%m-%d') > datetime.strptime(postData['end_date'], '%Y-%m-%d'):
        #     errors['end_date'] = 'End Date should be after the Start Date'

        if len(postData['plan']) < 3:
            errors['plan'] = "Plan must be at least 3 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip (models.Model):
    dest = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    plan = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="trips", on_delete = models.CASCADE)
    users_who_join = models.ManyToManyField(User, related_name="join_trip")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
     
