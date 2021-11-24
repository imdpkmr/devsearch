from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id':'1',
        'title':"Ecommerce Website",
        'description':"Fully functional ecommerce website",
    },
    {
        'id':'2',
        'title':"Portfolio Website",
        'description':"This was a project where I built out my protofolio",
    },
    {
        'id':'3',
        'title':"Social Network",
        'description':"Awesome open source project I am still working on",
    },
]

def projects(requests):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(requests, 'projects/projects.html', context)

def project(reqeusts, pk):
    projectObj = Project.objects.get(id=pk)
    return render(reqeusts, 'projects/project.html', {'project': projectObj}) 