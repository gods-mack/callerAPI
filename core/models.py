from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# user model with mobile number, name and email
class User(models.Model):
    phone       = PhoneNumberField(null=False, blank=False, unique=True)
    name        = models.CharField(max_length=20)
    email       = models.CharField(max_length=20, blank=True, null=True)
    password    = models.CharField(max_length=32, null=True)
    is_register = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.phone} {self.name}"



# global user info with phone number and name
class GlobalUser(models.Model):
    phone       = models.BigIntegerField(null=False, blank=False, db_index=True)
    name        = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.phone} {self.name}"



# spam score mapped with phone
class SpamScore(models.Model):
    phone = models.BigIntegerField(null=False, blank=True, db_index=True)
    spam_score = models.SmallIntegerField(default = 0)
    
    def __str__(self):
        return f"{self.phone}"



