from __future__ import absolute_import

from django.contrib import admin
from administrative.models import (
    Employee,
    Promissory
)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    '''Admin View for Employee'''

    list_display = (
        'employee_ID',
        'first_name',
        'last_name',
        'work_type',
        'emp_type',
        'emp_status',
    )
    list_filter = (
        'employee_ID',
        'first_name',
        'last_name',
        'work_type',
        'emp_type',
        'emp_status',
    )
    search_fields = (
        'employee_ID',
        'first_name',
        'last_name',
        'work_type',
        'emp_type',
        'emp_status',
    )
    ordering = (
        'employee_ID',
    )

@admin.register(Promissory)
class PromissoryAdmin(admin.ModelAdmin):
    '''Admin View for Promissory'''

    list_display = (
        'promissory_ID',
        'promissory_title',
        'reason',
        'date_filed',
        'date_approved',
        'due_of_payment',
        'student_ID',
        'schoolYr_ID',
        'promissory_status',
    )
    list_filter = (
        'promissory_ID',
        'promissory_title',
        'reason',
        'date_filed',
        'date_approved',
        'due_of_payment',
        'student_ID',
        'schoolYr_ID',
        'promissory_status',
    )
    search_fields = (
        'promissory_ID',
        'promissory_title',
        'reason',
        'date_filed',
        'date_approved',
        'due_of_payment',
        'student_ID',
        'schoolYr_ID',
        'promissory_status',
    )
    date_hierarchy = 'date_filed'
    ordering = (
        'promissory_ID',
        'promissory_title',
        'reason',
        'date_filed',
        'date_approved',
        'due_of_payment',
        'student_ID',
        'schoolYr_ID',
        'promissory_status',
    )