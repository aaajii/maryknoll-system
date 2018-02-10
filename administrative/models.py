from __future__ import unicode_literals

from django.db import models
#from registration.models import Student
#from enrollment.models import School_Year

# Create your models here.

CASHIER = 'c'
REGISTRAR = 'r'
ACADEMIC_HEAD = 'h'
TEACHER = 't'
OTHERS = 'n'

ACTIVE = 'a'
INACTIVE = 'i'
ON_LEAVE = 'o'

FULL_TIME = 'f'
PART_TIME = 'p'

class Employee(models.Model):
	employee_ID = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=50)
	
	
	TYPE_CHOICES = (
	    (CASHIER, 'Cashier'),
	    (REGISTRAR, 'Registrar'),
	    (ACADEMIC_HEAD, 'Academic Head'),
	    (TEACHER, 'Teacher'),
	    (OTHERS, 'Others'),
	)
	emp_type = models.CharField(max_length=1,
	    choices=TYPE_CHOICES,
	    blank=False,
	    default=OTHERS
	    )

	STATUS_CHOICES = (
	    (ACTIVE, 'Active'),
	    (ON_LEAVE, 'On Leave'),
	    (INACTIVE, 'Inactive'),
	)
	emp_status = models.CharField(max_length=1,
	    choices=STATUS_CHOICES,
	    blank=False,
	    default=INACTIVE
	    )
        
	
	class Meta:
		verbose_name = "Employee"
		
	def __str__(self):
		return self.first_name
	
ON_HOLD = "h"
APPROVED = "p"
DECLINED = "d"

class Promissory(models.Model):
	promissory_ID = models.AutoField(primary_key=True)
	promisorry_title = models.CharField(max_length=200)
	reason = models.CharField(max_length=500)
	date_filed = models.DateTimeField(null=True, blank=True, auto_now = True)
	date_approved = models.DateTimeField(null=True, blank=True, auto_now = True)
	due_of_payment = models.DateTimeField(null=True, blank=True)
	student_ID = models.ForeignKey('registration.Student', on_delete=models.CASCADE, default=0)
	schoolYr_ID = models.ForeignKey('enrollment.School_Year', on_delete=models.CASCADE, default=0)
	STATUS_CHOICES = (
	    (ON_HOLD, 'On Hold'),
	    (APPROVED, 'Approved'),
	    (DECLINED, 'Declined'),
	)
	emp_status = models.CharField(max_length=1,
	    choices=STATUS_CHOICES,
	    blank=False,
	    default=ON_HOLD
	    )
	
	class Meta:
		verbose_name = "Promissory Note"
		
	def __str__(self):
		return self.promisorry_title