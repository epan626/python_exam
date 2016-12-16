from __future__ import unicode_literals
from ..regandlogin.models import User
from django.db import models

# Create your models here.

class ProductManager(models.Manager):
    def validate_product(self, form_data):
        errors = []
        user = Product.objects.filter(name = form_data['product'])
        if len(form_data['product']) == 0:
            errors.append('Item can not be blank!')
        if len(form_data['product']) <= 3:
            errors.append('Item has be over 3 characters!')
        return errors

class Product(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('regandlogin.User', related_name='user__product', null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()
