from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

def main(request):

    projects = Project.objects.all()

    context = {'projects': projects}
    return render(request, 'main/main.html', context)