from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=128)  # Storing hashed passwords
    # date_of_birth = models.DateField(blank=True, null=True)
    # phone_number = models.CharField(max_length=15, blank=True)
    
    def _str_(self):
        return self.name


class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=40)
    mobile = models.CharField(max_length=10)  # Assuming a maximum length for mobile number
    message = models.TextField()

    def _str_(self):
        return self.full_name