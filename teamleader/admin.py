from django.contrib import admin
from .models import team_leader,project,task,team_member
# Register your models here.

admin.site.register(team_leader)
admin.site.register(team_member)
admin.site.register(project)
admin.site.register(task)
