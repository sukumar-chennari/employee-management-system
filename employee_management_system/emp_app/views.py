from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from .models import *
from django.contrib import messages
from datetime import datetime
from django.db.models import Q

 
# Create your views here.
def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        role=request.POST['role']
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        phone=request.POST['phone']
        dept=request.POST['department']
        

        new_emp=Employee(
                first_name=first_name,
                last_name=last_name,
                role_id=role,
                salary=salary,
                bonus=bonus,
                phone=phone,
                dept_id=dept,
                
                hire_date=datetime.now()
                )
        new_emp.save()
        messages.info(request,'Employee added Successfully!!!')

    return render(request,'add_emp.html')

def remove_emp(request,id=0):
    
    if id:
        try:
            emp_to_be_removed=Employee.objects.get(id=id)
            emp_to_be_removed.delete()
            messages.info(request,'Emplyed removed Succesfully')
        except:
            messages.info(request,'Select valid Employee')
    emps=Employee.objects.all()
    context={"emps":emps}
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(Q(dept__name__icontains=dept))
        if role:
            emps=emps.filter(Q(roe__name__icontains=role))
        context={'emps':emps}
        return render(request,'all_emp.html',context)
    return render(request,'filter_emp.html')