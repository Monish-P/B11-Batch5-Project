from django.shortcuts import redirect, render,HttpResponse
from .models import team_leader,team_member,project,task
# Create your views here.

def create_project(request,id):
    title = request.POST.get('title')
    userid = request.POST.get('userid')
    tl = team_leader.objects.get(user_id = userid)
    project.objects.create(name = title, project_teamleader = tl)
    tl.is_project_created = True
    tl.save()
    return redirect('team_leader_dashboard',id)

def delete_project(request,id):
    tl = team_leader.objects.get(id=id)
    pro = project.objects.get(project_teamleader = tl)
    tl.is_project_created = False
    tl.save()
    pro.delete()
    return redirect('team_leader_dashboard',id)

def return_tl_update_page(request,id):
    tl = team_leader.objects.get(id = id)
    return render(request,'teamleader/update_details.html',context={'tl':tl})

def update_details(request,id):
    name = request.POST.get('name')
    password = request.POST.get('password')
    email = request.POST.get('email')

    tl = team_leader.objects.get(id=id)
    tl.name = name
    tl.email = email
    tl.password = password
    tl.save()
    return redirect('tl_update_page',id)

def return_add_teammembers_page(request,id):
    tl = team_leader.objects.get(id = id)
    return render(request,'teamleader/add_team_mem.html',context={'tl':tl})

def add_team_members(request,id):
    userid = request.POST.get('userid')
    tm = team_member.objects.get(user_id = userid)
    tl = team_leader.objects.get(id=id)
    tm.team_of = tl
    tm.is_team_assigned = True
    tm.save()
    return redirect('team_leader_dashboard',id)

def return_add_tasks_page(request,id):
    tl = team_leader.objects.get(id = id)
    return render(request,'teamleader/add_tasks.html',context={'tl':tl,'tms':team_member.objects.filter(team_of = tl)})

def add_tasks(request,id):
    name = request.POST.get('name')
    points = request.POST.get('points')
    assigned_to = request.POST.get('assigned_to')
    desc = request.POST.get('description')
    tl = team_leader.objects.get(id=id)
    pro = project.objects.get(project_teamleader = tl)
    task.objects.create(name = name,description = desc, task_of = pro, points = points,assigned_to = team_member.objects.get(user_id=\
        assigned_to))
    pro.no_of_pending_tasks += 1
    pro.save()
    return redirect('team_leader_dashboard',id)
    
def return_approve_page(request,id):
    tl = team_leader.objects.get(id = id)
    return render(request,'teamleader/approve_tasks.html',context={'tl':tl,'tasks':task.objects.filter(task_of = \
        project.objects.get(project_teamleader = tl),status = 1)})

def approve_task(request,id,task_id):
    t = task.objects.get(id = task_id)
    tm = t.assigned_to
    tm.total_points += t.points
    t.status = 2
    tm.no_of_tasks_accepted+=1
    tm.save()
    t.save()
    tl = team_leader.objects.get(id = id)
    pro = project.objects.get(project_teamleader = tl)
    pro.no_of_pending_tasks -= 1
    pro.no_of_tasks_completed += 1
    pro.save()
    return redirect('approve_page',id)

def disapprove_task(request,id,task_id):
    t = task.objects.get(id = task_id)
    tm = t.assigned_to
    tm.no_of_tasks_rejected+=1
    t.status = 0
    tm.save()
    t.save()
    return redirect('approve_page',id)