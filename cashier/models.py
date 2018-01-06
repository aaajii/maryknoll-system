from __future__ import unicode_literals

from django.db import models
from registration.models import Enrollment

# Create your models here.
'''TAIL ENTITIES'''
class FeesAccounts(models.Model):
    fa_ID = models.AutoField(primary_key = True)
    fa_name = models.CharField(max_length = 200)
    amount = models.FloatField()
    
'''NON-TAIL ENTITIES'''

class Payments(models.Model):
    payment_ID = models.AutoField(primary_key=True)
    enrollment_ID = models.ForeignKey(Enrollment, on_delete = models.SET_NULL, null = True)
    payment_date = models.DateField()
    total_amount = models.FloatField()
    payment_type = models.CharField(max_length=200)
    payment_note = models.CharField(max_length=200)
    OR_number = models.IntegerField()
    
class PaymentDetails(models.Model):
    pdetails_ID = models.AutoField(primary_key=True)
    payment_ID = models.ForeignKey(Payment, on_delete = models.SET_NULL, null = True)
    fa_ID = models.ForeignKey(FeesAccounts, on_delete=models.SET_NULL, null=True)