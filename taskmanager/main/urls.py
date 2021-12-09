from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path(r'', views.index, name='home'),

    path(r'faculty/', views.faculty, name="faculty"),
    path(r'showfaculty/<int:id>/', views.showfaculty, name="showfaculty"),
    path(r'showfaculty/delete/<int:id>/', views.deletefaculty, name="deletefaculty"),

    path(r'department/', views.department, name="department"),
    path(r'showdepartment/<int:id>/', views.showdepartment, name="showdepartment"),
    path(r'showdepartment/delete/<int:id>/', views.deletedepartment, name="deletedepartment"),

    path(r'group/', views.group, name="group"),
    path(r'showgroup/<int:id>/', views.showgroup, name="showgroup"),
    path(r'showgroup/delete/<int:id>/', views.deletegroup, name="deletegroup"),

    path(r'student/', views.student, name="student"),
    path(r'showstudent/<int:id>/', views.showstudent, name="showstudent"),
    path(r'showstudent/delete/<int:id>/', views.deletestudent, name="deletestudent"),

    path(r'fellow/', views.fellow, name="fellow"),
    path(r'showfellow/<int:id>/', views.showfellow, name="showfellow"),
    path(r'showfellow/delete/<int:id>/', views.deletefellow, name="deletefellow"),

    path(r'accrual/', views.accrual, name="accrual"),
    path(r'showaccrual/<int:id>/', views.showaccrual, name="showaccrual"),
    path(r'showaccrual/delete/<int:id>/', views.deleteaccrual, name="deleteaccrual"),


    path(r'reports/', views.reports, name='reports'),
    path(r'reports/editstaff/<int:id>/', views.editstaff, name='editstaff'),
    path(r'reports/deletestaff/<int:id>/', views.deletestaff, name='deletestaff'),
    
    path(r'reports/showfund/<int:id>/', views.showfund, name='showfund'),

    path(r'authorization/', views.user_login, name='login'),
    path(r'logout/', LogoutView.as_view(next_page='/'), name='logout'),


    path(r'authorization/', views.authorization, name='authorization'),
]
