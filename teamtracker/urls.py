"""teamtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teammember import views as tmviews
from teamleader import views as tlviews
from manager import views as mviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mviews.login,name='login'),
    path('check_login',mviews.check_login,name='check_login'),
    path('logout',mviews.logout_view,name='logout'),
    path('register',mviews.register_view,name='register'),
    path('team_member_default',mviews.create_teammember,name='team_member_default'),
    path('team_leader_dashboard/<int:id>/',mviews.team_leader_dashboard,name='team_leader_dashboard'),
    path('team_member_dashboard/<int:id>/',mviews.team_member_dashboard,name='team_member_dashboard'),
    path('team_leader_dashboard/<int:id>/create_project',tlviews.create_project,name='create_project'),
    path('team_leader_dashboard/<int:id>/delete_project',tlviews.delete_project,name='delete_project'),
    path('team_leader_dashboard/<int:id>/tl_update_page',tlviews.return_tl_update_page,name = 'tl_update_page'),
    path('team_leader_dashboard/<int:id>/tl_update_details',tlviews.update_details,name = 'tl_update_details'),
    path('team_leader_dashboard/<int:id>/add_teammembers_page',tlviews.return_add_teammembers_page,name = 'add_teammembers_page'),
    path('team_leader_dashboard/<int:id>/add_teammembers',tlviews.add_team_members,name = 'add_teammembers'),
    path('team_leader_dashboard/<int:id>/add_tasks_page',tlviews.return_add_tasks_page,name = 'add_tasks_page'),
    path('team_leader_dashboard/<int:id>/add_tasks',tlviews.add_tasks,name = 'add_tasks'),
    path('team_member_dashboard/<int:id>/tm_update_page',tmviews.return_update_page,name = 'tm_update_page'),
    path('team_member_dashboard/<int:id>/tm_update',tmviews.update_team_member,name = 'tm_update'),
    path('team_member_dashboard/<int:id>/task/<int:task_id>/',tmviews.return_detail_page,name = 'task'),
    path('team_member_dashboard/<int:id>/task/<int:task_id>/send_approval',tmviews.send_approval,name = 'send_approval'),
    path('team_leader_dashboard/<int:id>/approve_page',tlviews.return_approve_page,name = 'approve_page'),
    path('team_leader_dashboard/<int:id>/approve/<int:task_id>/',tlviews.approve_task,name = 'approve_task'),
    path('team_leader_dashboard/<int:id>/disapprove/<int:task_id>/',tlviews.disapprove_task,name = 'disapprove_task'),
    path('manager_dashboard',mviews.manager_dashboard,name="manager_dashboard"),
    path('team_details/<int:pro_id>/',mviews.team_details,name = 'team_details'),
    path('team_details/<int:pro_id>/delete_team/<int:tl_id>/',mviews.delete_team,name = 'delete_team'),
    path('create_team_page',mviews.return_create_team_page,name = 'create_team_page'),
    path('create_team',mviews.create_team,name = 'create_team'),
    path('about',mviews.about,name = 'about'),
    path('bar_chart',mviews.bar_chart,name='bar_chart'),
    path('forgot_password',mviews.return_forgot_password_page,name='forgot_password'),
    path('check_phone_num',mviews.check_phone_num,name='check_phone_num'),
    path('check_otp/<int:id>/',mviews.check_otp,name='check_otp'),
    path('check_otp/<int:id>/change_password',mviews.change_password,name='change_password'),





]
