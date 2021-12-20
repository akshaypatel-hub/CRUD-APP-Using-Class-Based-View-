from django.db import models
from django.urls import reverse
# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password =models.CharField(max_length=20)

    # def get_absolute_url(self):
    #     return reverse("details" , kwargs={"pk": self.pk})