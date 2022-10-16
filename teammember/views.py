from django.shortcuts import render,HttpResponse,redirect
from teamleader.models import team_leader,team_member,project,task
# Create your views here.

def return_update_page(request,id):
    tm = team_member.objects.get(id=id)
    return render(request,'teammember/update.html',context = {'tm':tm})

def update_team_member(request,id):
    name = request.POST.get('name')
    email = request.POST.get('email')
    userid = request.POST.get('userid')
    password = request.POST.get('password')

    tm = team_member.objects.get(id=id)
    tm.name = name
    tm.email = email
    tm.password = password
    tm.user_id = userid
    tm.save()

    return redirect('tm_update_page',id)

def return_detail_page(request,id,task_id):
    t = task.objects.get(id = task_id)
    tm = team_member.objects.get(id=id)

    return render(request,'teammember/task_detail.html',context = {'task': t,'tm': tm})

def send_approval(request,id,task_id):
    t = task.objects.get(id = task_id)
    t.status = 1
    t.save()
    return redirect('team_member_dashboard',id)




