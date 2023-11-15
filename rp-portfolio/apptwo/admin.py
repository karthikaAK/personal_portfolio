from django.contrib import admin

# Register your models here.

from django.contrib import admin
from apptwo.models import Project

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)