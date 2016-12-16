from __future__ import unicode_literals
from django.db import models
import bcrypt, re

name_regex = re.compile(r'^[a-zA-Z_ ]+$')

# Create your models here.

class UserManager(models.Manager):
    def validate_registration(self, form_data):
        errors = []
        user = User.objects.filter(username = form_data['username'])
        if len(form_data['name']) == 0:
            errors.append('Name is required!')
        if len(form_data['name']) < 3:
            errors.append('Name has be over 3 characters!')
        elif not name_regex.match(form_data['name']):
            errors.append('Your name has to be letters')

        if len(form_data['username']) == 0:
            errors.append('Username is required!')
        if len(form_data['username']) < 3:
            errors.append('Username has to be over 3 characters!')
        elif not name_regex.match(form_data['username']):
            errors.append('Username has to be letters')
        elif len(user) > 0:
            errors.append('This username already exist in the system!')

        if len(form_data['password']) == 0:
            errors.append('Password is required!')
        elif len(form_data['password']) < 8:
            errors.append('Your password cannot be less than 8 characters!')

        if len(form_data['conpassword']) == 0:
            errors.append('Password Confirmation is required!')
        elif form_data['conpassword'] != form_data['password']:
            errors.append('Your password fields do not match!')

        return errors

    def register(self, form_data):
        hashed_pass = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())
        return self.create(name=form_data['name'], username=form_data['username'], password=hashed_pass)

    def check_login(self, form_data):
        check_user = self.filter(username=form_data['username'])
        if check_user:
            user = check_user[0]
            if bcrypt.hashpw(form_data['password'].encode(), user.password.encode()) == user.password:
                return user
        return None
    def logout(self):
        pass

class User(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    wish = models.ManyToManyField('products.Product', related_name='user__wish')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
