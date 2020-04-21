from django.contrib.auth.models import User
from django.db import models


class File(models.Model):
    title = models.CharField(max_length=50)
    profile = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='files'
    )
    upload = models.FileField(upload_to='files/')
