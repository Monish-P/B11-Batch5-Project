from django.shortcuts import render,redirect,HttpResponse
from teamleader.models import team_leader,team_member,project,task
from django.contrib.auth import logout
from django.http import JsonResponse
# Create your views here.
def login(request):
    return render(request,'manager/login.html')

def check_login(request):
    userid   = request.POST.get('userid')
    password = request.POST.get('password')
    if userid == 'admin' and password == 'admin':
        return redirect('manager_dashboard')
    elif userid[:2] == 'tl' and  team_leader.objects.filter(user_id=userid).exists():
        tl = team_leader.objects.get(user_id=userid)
        if tl.password == password:
            return redirect('team_leader_dashboard',tl.id)
        else:
            return HttpResponse('Invalid userid or password!')
    elif team_member.objects.filter(user_id=userid).exists():

        tm = team_member.objects.get(user_id=userid)
        if tm.password == password:
            if tm.is_team_assigned:
                return redirect('team_member_dashboard',tm.id)
            else:
                return render(request,'teammember/default.html')
        else:
            return HttpResponse('Invalid userid or password!')
    else:
        return HttpResponse('Invalid userid or password!')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    return render(request,'manager/register.html')

def create_teammember(request):
    name = request.POST.get('name')
    userid   = request.POST.get('userid')
    email = request.POST.get('email')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')
    if userid[:2] == 'tl' or team_member.objects.filter(user_id=userid).exists():
        return HttpResponse("Please Choose other userid")
    if password != cpassword:
        return HttpResponse("Please enter correct password")
    team_member.objects.create(name=name, user_id=userid,password=password,email=email)
    return render(request,'teammember/default.html')

def team_leader_dashboard(request,id):
    tl = team_leader.objects.get(id=id)
    if project.objects.filter(project_teamleader = tl).exists():
        pro = project.objects.get(project_teamleader = tl)
        try:
            progress = (pro.no_of_tasks_completed * 100) / (pro.no_of_tasks_completed + pro.no_of_pending_tasks)
        except Exception:
            progress = 0
        pro.progress = progress
        pro.save()
        context = {
        'tl': tl,
        'tms': team_member.objects.filter(team_of = tl),
        'project': pro,
        'pend_tasks': task.objects.filter(task_of = pro, status = 0),
        'comp_tasks': task.objects.filter(task_of = pro, status = 2),
        'progress': int(progress),

        }
    else:
        context = {
            'tl': tl,
            'tms': team_member.objects.filter(team_of = tl)
        }
    return render(request,'teamleader/dashboard.html',context)

def team_member_dashboard(request,id):
    tm = team_member.objects.get(id = id)
    comp = task.objects.filter(assigned_to = tm,status = 2).count()
    appr = task.objects.filter(assigned_to = tm,status = 1).count()
    pend = task.objects.filter(assigned_to = tm,status = 0).count()
    data = [comp,appr,pend]
    labels = ["completed","need to be approved","pending"]
    pdata = [tm.no_of_tasks_accepted,tm.no_of_tasks_rejected]
    plabels = ["Tasks Accepted","Tasks Rejected"]
    try:
        eff = (tm.no_of_tasks_accepted * 100) / (tm.no_of_tasks_accepted+tm.no_of_tasks_rejected)
    except Exception:
        eff = 0
    pro = project.objects.get(project_teamleader = tm.team_of)
    tms = team_member.objects.order_by('-total_points')[:5]
    context = {
        'tasks': task.objects.filter(assigned_to = tm),
        'tm': tm,
        'pro': pro,
        'labels':labels,
        'data':data,
        'pdata': pdata,
        'plabels': plabels,
        'eff': eff,
        'tms': tms,
    }
    return render(request,'teammember/dashboard.html',context)
def bar_chart(request):
    labels = []
    data = []
    projects = project.objects.all()
    for pro in projects:
        labels.append(pro.project_teamleader.team_name)
        data.append(pro.progress)
    return JsonResponse(data={
        'labels': labels,
        'data': data
    })
def manager_dashboard(request):
    projects = project.objects.all()
    context = {
        'projects': projects,
        'tms': team_member.objects.all()
    }
    return render(request,'manager/dashboard.html',context)
def team_details(request,pro_id):
    pro = project.objects.get(id = pro_id)
    context = {
        'pro': pro,
        'pending_tasks': task.objects.filter(task_of = pro,status = 0),
        'completed_tasks': task.objects.filter(task_of = pro,status = 2)
    }
    return render(request,'manager/Details.html',context)

def delete_team(request,pro_id,tl_id):
    tl = team_leader.objects.get(id = tl_id)
    tl.delete()

    return redirect('manager_dashboard')

def return_create_team_page(request):
    return render(request,'manager/Create_Team.html')

def create_team(request):
    name = request.POST.get("name")
    team_name = request.POST.get("team_name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    userid = request.POST.get("userid")

    team_leader.objects.create(name = name, team_name = team_name, user_id = userid,password = password,email = email)
    return redirect('manager_dashboard')

def about(request):
    return render(request,'manager/about.html')

