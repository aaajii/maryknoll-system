from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmployeeForms
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import *
from django.db.models import Q

#GLOBAL FUNCTIONS
def ajaxTable(request, template, context, data = None):
    # For templates that needs ajax
    html_form = render_to_string(template,
        context,
        request = request,
    )
    if data:
        data['html_form'] = html_form
    else:
        data = {'html_form' : html_form}
    return JsonResponse(data)
def updateInstance(request, modelForm, instance):
    if request.method == 'POST':
        form = modelForm(request.POST, instance = instance)
        if form.is_valid():
            instance = form.save()
            instance.save()
    else:
        form = modelForm(instance = instance)
    return form
def getLatest(model, attribute):
    # Get latest record of a model, basing on a certain attribute
    # Returns an instance
    try:
        latest = model.objects.latest(attribute)
    except:
        latest = None
    return latest
def paginateThis(request, obj_list, num):
    # Pagination. Send request, the list you want to paginate, and number of items per page.
    # This returns a limited list with pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(obj_list, num)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)
    return lists
#---------------



@login_required
def index(request):
    pass

@login_required
def userList(request):
    return render(request, 'administrative/admin-employee-list.html')

def addEmployeeProfile(request):
    return render(request, 'administrative/admin-employee-list-add.html')

def updateEmployee(request, pk='pk'):
    instance = get_object_or_404(Employee, pk=pk)
    return render(request, 'administrative/admin-employee-list-update.html', {'instance': instance})


    
#AJAX VIEWS --------------------------------------------------------------------
from django.template.loader import render_to_string
from django.http import JsonResponse

def tableEmployeeList(request):
    employee_list = getEmployeeList(request)
    #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(employee_list, 5)
    
    try:
        employee = paginator.page(page)
    except PageNotAnInteger:
        employee = paginator.page(1)
    except EmptyPage:
        employee = paginator.page(paginator.num_pages)
        
    context = {'employee_list': employee}
    html_form = render_to_string('administrative/table-employee-list.html',
        context,
        request = request,
    )
    return JsonResponse({'html_form' : html_form})

def createEmployeeProfile(request):
    data = {'form_is_valid' : False }
    try:
        last_employee = Employee.objects.latest('employee_ID')
    except:
        last_employee = None
    if request.method == 'POST':
        form = EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = EmployeeForms()
    context = {'form': form, 'employee':last_employee}
    data['html_form'] = render_to_string('administrative/forms-employee-create.html',
        context,
        request=request,
    )
    return JsonResponse(data)
    
def updateEmployeeForm(request, pk='pk'):
    instance = get_object_or_404(Employee, pk=pk)
    data = {'form_is_valid' : False }
    try:
        last_employee = Employee.objects.latest('employee_ID')
    except:
        last_employee = None
    if request.method == 'POST':
        form = EmployeeForms(request.POST, instance = instance)
        if form.is_valid():
            instance = form.save()
            instance.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = EmployeeForms(instance = instance)
    context = {'form': form, 'employee':last_employee, 'instance': instance}
    data['html_form'] = render_to_string('administrative/forms-employee-update.html',
        context,
        request=request,
    )
    return JsonResponse(data)

def getEmployeeList(request):
    search = request.GET.get('search')
    genre = request.GET.get('genre')
    isNum = True
    try:
        int(search)
    except:
        isNum = False
    if(request.GET.get('search')!= "None"):
        if( (genre == "None" or genre == "All Categories") and isNum):
            query = Employee.objects.filter(
                Q(employee_ID__contains=search)|
                Q(first_name__contains=search)|
                Q(last_name__contains=search)|
                Q(work_type__contains=search)|
                Q(emp_type__contains=search)|
                Q(emp_status__contains=search)
            )
        if(genre == "None" or genre == "All categories"):
            query = Employee.objects.filter(
                Q(employee_ID__contains=search)|
                Q(first_name__icontains=search)|
                Q(last_name__icontains=search)|
                Q(work_type__contains=search)|
                Q(emp_type__contains=search)|
                Q(emp_status__contains=search)
            )
        elif(genre == "Full Name"):
            query = Employee.objects.filter(
                Q(first_name__icontains=search)|
                Q(last_name__icontains=search)
            )
        elif(genre == "Employee Type"):
            query = Employee.objects.filter(emp_type=search)
        elif(genre == "Work Type"):
            query = Employee.objects.filter(work_type=search)
            if (search == ""):
                query = Employee.objects.all()
        elif(genre == "Status"):
            query = Employee.objects.filter(emp_status=search)
        else:
            query = Employee.objects.all()
    else:
        return []
    return query
    

def employeeDetails(request,pk,template="administrative/employee-profile.html"):
    employee = Employee.objects.get(pk=pk)
    context = {'employee':employee}
    return render(request,template,context)

# SYSTEM USERS

def usersList(request,template='administrative/system-users/users-list.html'):
    context = {}
    return render(request,template,context)

def tableUsersList(request,template='administrative/system-users/table-users-list.html'):
    context = {}
    return ajaxTable(request,template,context)

def addSystemUser(request,template='administrative/system-users/users-list-add.html'):
    context={}
    return render(request,template,context)