from django.db import models
import re
from django.core.exceptions import ValidationError


def validate_login(login):
    pattern = r"[a-zA-Z0-9]{6,}$"
    if re.match(pattern, login) is None:
        raise ValidationError('Логин задан не верно')


def validate_email(email):
    pattern = "^[-\\w\\.]+@[-\\w]+\\.+[-\\w]{2,}$"
    if re.match(pattern, email) is None:
        raise ValidationError('Email задан не верно')


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=30)
    login = models.CharField(max_length=100, null=True, validators=[
        validate_login
    ])
    email = models.CharField(max_length=100, null=True, validators=[
        validate_email
    ])
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    category_title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category_title}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
