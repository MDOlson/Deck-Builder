from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postdata):
        errors = {}   
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postdata['fname']) < 2:
            errors['fname'] = "First name must be at least 2 characters"

        if len(postdata['lname']) < 2:
            errors['lname'] = "Last name must be at least 2 characters"
        
        if not EMAIL_REGEX.match(postdata['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        
        if len(postdata['pw']) < 8:
            errors["pw"] = "Password must be at least 10 characters"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()

# class Deck(models.Model):
#     height = models.height
#     length = models.length
#     width = models.width
#     decking = models.decking
#     spacing = models.spacing
#     flashing = models.flashing
#     hang_n_nails = models.hang_n_nails
#     screws = models.screws
#     lag_bolts = models.lag_bolts