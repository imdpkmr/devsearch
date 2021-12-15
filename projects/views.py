from django.contrib.auth import login
from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from .utils import searchProjects, paginateProjects

def projects(request):
    search_query, projects = searchProjects(request)
    custom_range, projects, paginator = paginateProjects(request, projects, 5)    
    context = {'projects':projects, 'search_query':search_query, 'paginator':paginator, 'custom_range':custom_range}
    return render(request, 'projects/projects.html', context)

def project(reqeust, pk):
    projectObj = Project.objects.get(id=pk)
    return render(reqeust, 'projects/project.html', {'project': projectObj}) 

# the following decorator will restrict the access of the below view to only signed in users
@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
            
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, "delete_template.html", context)