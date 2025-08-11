from django.db import models

class plot(models.Model):
    Name=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    Image=models.CharField(max_length=2500)
