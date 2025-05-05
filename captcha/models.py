from django.db import models


# Create your models here.
class verified(models.Model):
    name = models.CharField(max_length = 100,blank = False)
    email = models.EmailField(blank = False)