

from django.db import models
# Create your models here.

class team_leader(models.Model):
    name = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    is_project_created = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class team_member(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    total_points = models.IntegerField(default = 0)
    is_team_assigned = models.BooleanField(default=False)
    team_of = models.ForeignKey(team_leader,on_delete = models.CASCADE,blank = True, null = True)
    no_of_tasks_accepted = models.IntegerField(default = 0)
    no_of_tasks_rejected = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class project(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default = True)
    date_created = models.DateTimeField(auto_now_add=True)
    no_of_pending_tasks = models.IntegerField(default = 0)
    no_of_tasks_completed = models.IntegerField(default = 0)
    project_teamleader = models.OneToOneField(team_leader,on_delete = models.CASCADE)
    progress = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length = 500)
    task_of = models.ForeignKey(project,on_delete = models.CASCADE)
    points = models.IntegerField()
    assigned_to = models.ForeignKey(team_member,on_delete = models.CASCADE)
    status = models.IntegerField(default = 0)

    def __str__(self):
        return self.name


