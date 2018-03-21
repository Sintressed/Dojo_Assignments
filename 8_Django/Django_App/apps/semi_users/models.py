# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
# Create your models here.


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) or len(postData['last_name']) or len(postData['email_address'])== 0:
            errors["name"] = "EYYYYY! DONT PUT ANY EMPTIES IN HERE BOI"
        else:
            errors.clear()
        if not EMAIL_REGEX.match(postData['email_address']):
            errors["email"] = "Email address invalid"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
