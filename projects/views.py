from django.shortcuts import render
from django.http import HttpResponse


def projects(requests):
    return render(requests, 'projects/projects.html')

def project(reqeusts, pk):
    return render(reqeusts, 'projects/project.html')