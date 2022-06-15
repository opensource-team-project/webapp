
from statistics import mode
from django.db import models
from django.forms import PasswordInput
from django.contrib.auth.models import User

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length = 500)
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    writter = models.ForeignKey(User, related_name='documents',on_delete=models.CASCADE, null=True) 

