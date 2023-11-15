from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from apptwo.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        "apptwo":projects
    }
    return render(request,"apptwo/project_index.html",context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "apptwo": project
    }
    return render(request, "apptwo/project_detail.html", context)