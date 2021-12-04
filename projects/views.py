from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from users.models import User
from django.contrib.auth.decorators import login_required


def projects(requests):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(requests, 'projects/projects.html', context)

def project(reqeusts, pk):
    projectObj = Project.objects.get(id=pk)
    return render(reqeusts, 'projects/project.html', {'project': projectObj}) 

# the following decorator will restrict the access of the below view to only signed in users
@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
            
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, "projects/delete_template.html", context)