from django.shortcuts import render
from django.http import HttpResponse


def projects(requests):
    return HttpResponse('Here are our projects')

def project(reqeusts, pk):
    return HttpResponse("Here is our project"+"  "+pk)