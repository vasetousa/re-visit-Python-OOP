from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse('This is home')


def department(request, id):
    return HttpResponse(f'This is department {id}')


def department_details(request):
    return HttpResponse('Details of this department')


def department_list(request):
    return HttpResponse('Listing all departments')


def create_department(request):
    return HttpResponse('Creating a department')


def update_department(request):
    return HttpResponse('Updating a department')


def delete_department(request):
    return HttpResponse('Deleting a department')
