from datetime import date, timedelta

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import *
from .forms import LoginForm
from .models import *

# Create your views here.


def modelobjects():
    try:
        bank_model = Bank.objects.all()[::-1]
        educ_type_model = Types_of_Education.objects.all()[::-1]
        scholar_type_model = Types_of_Scholarship.objects.all()[::-1]
        staff_model = Staff.objects.all()[::-1]
        faculty_model = Faculty.objects.all()[::-1]
        department_model = Department.objects.all()[::-1]
        group_model = Group.objects.all()[::-1]
        student_model = Student.objects.all()[::-1]
        accrual_model = Accrual.objects.all()[::-1]
        scholar_fund_model = Scholarship_Fund.objects.all()[::-1]
        fellow_model = Fellow.objects.all()[::-1]
    except:
        raise Http404("Question does not exist")
    context = {
        'bank_model': bank_model,
        'educ_type_model': educ_type_model,
        'scholar_type_model': scholar_type_model,
        'staff_model': staff_model,
        'faculty_model': faculty_model,
        'department_model': department_model,
        'group_model': group_model,
        'student_model': student_model,
        'accrual_model': accrual_model,
        'scholar_fund_model': scholar_fund_model,
        'fellow_model': fellow_model,
    }
    return context


def index(request):
    return render(
        request,
        'main/index.html'
    )

# Факультеты


def faculty(request):
    faculty_model = Faculty.objects.all()
    if request.method == 'GET':
        form = FacultyForm()
    elif request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            faculty_model = form.save(commit=False)
            faculty_model.faculty_name = form.cleaned_data['faculty_name']
            faculty_model.deanery_employee_code = form.cleaned_data['deanery_employee_code']
            faculty_model.save()
            return redirect('faculty')
    return render(
        request,
        'main/faculty.html',
        {
            'form': form,
            'faculty_model': faculty_model[::-1]
        }
    )


def showfaculty(request, id):
    try:
        post = get_object_or_404(Faculty, pk=id)
        slaves = Department.objects.filter(faculty_code=id)
        if request.method == 'GET':
            form = FacultyForm(instance=post)
        elif request.method == 'POST':
            form = FacultyForm(request.POST, instance=post)
            if form.is_valid():
                # post.faculty_name = form.cleaned_data['faculty_name']
                # post.deanery_employee_code = form.cleaned_data['deanery_employee_code']
                form.save()
                return HttpResponseRedirect(reverse('showfaculty', args=(id,)))
        context = {
            'post': post,
            'form': form,
            'slaves': slaves,
        }
        return render(
            request,
            'main/showfaculty.html',
            context
        )
    except Staff.DoesNotExist:
        return HttpResponseNotFound("<h2>Person no found</h2>")


@login_required
def deletefaculty(request, id):
    try:
        staff = Faculty.objects.get(pk=id)
        staff.delete()
        return redirect('faculty')
    except Faculty.DoesNotExist:
        return HttpResponseNotFound("<h2>this person not found</h2>")

# Кафедры


def department(request):
    department_model = Department.objects.all()
    if request.method == 'GET':
        form = DepartmentForm()
    elif request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department_model = form.save(commit=False)
            department_model.department_name = form.cleaned_data['department_name']
            department_model.faculty_code = form.cleaned_data['faculty_code']
            department_model.department_head_code = form.cleaned_data['department_head_code']
            department_model.save()
            return redirect('department')
    return render(
        request,
        'main/department.html',
        {
            'form': form,
            'department_model': department_model[::-1],
        }
    )


def showdepartment(request, id):
    try:
        post = get_object_or_404(Department, pk=id)
        slaves = Group.objects.filter(issuing_department_code=id)
        if request.method == 'GET':
            form = DepartmentForm(instance=post)
        elif request.method == 'POST':
            form = DepartmentForm(request.POST, instance=post)
            if form.is_valid():
                # post.department_name = form.cleaned_data['department_name']
                # post.faculty_code = form.cleaned_data['faculty_code']
                # post.department_head_code = form.cleaned_data['department_head_code']
                form.save()
                return HttpResponseRedirect(reverse('showdepartment', args=(id,)))
        context = {
            'post': post,
            'form': form,
            'slaves': slaves,
        }
        return render(
            request,
            'main/showdepartment.html',
            context
        )
    except Staff.DoesNotExist:
        return HttpResponseNotFound("<h2>Person no found</h2>")


@login_required
def deletedepartment(request, id):
    try:
        dep = Department.objects.get(pk=id)
        dep.delete()
        return redirect('department')
    except Faculty.DoesNotExist:
        return HttpResponseNotFound("<h2>this person not found</h2>")

# Группы


def group(request):
    group_model = Group.objects.all()
    if request.method == 'GET':
        form = GroupForm()
    elif request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group_model = form.save(commit=False)
            group_model.group_name = form.cleaned_data['group_name']
            group_model.issuing_department_code = form.cleaned_data['issuing_department_code']
            group_model.сurator_code = form.cleaned_data['сurator_code']
            group_model.save()
            return redirect('group')
    return render(
        request,
        'main/group.html',
        {
            'form': form,
            'group_model': group_model[::-1]
        }
    )


def showgroup(request, id):
    try:
        post = get_object_or_404(Group, pk=id)
        slaves = Student.objects.filter(group_code=id)
        if request.method == 'GET':
            form = GroupForm(instance=post)
        elif request.method == 'POST':
            form = GroupForm(request.POST, instance=post)
            if form.is_valid():
                # post.group_name = form.cleaned_data['group_name']
                # post.group_head_student_code = form.cleaned_data['group_head_student_code']
                # post.issuing_department_code = form.cleaned_data['issuing_department_code']
                # post.сurator_code = form.cleaned_data['сurator_code']
                form.save()
                return HttpResponseRedirect(reverse('showgroup', args=(id,)))
        context = {
            'post': post,
            'form': form,
            'slaves': slaves,
        }
        return render(
            request,
            'main/showgroup.html',
            context
        )
    except Staff.DoesNotExist:
        return HttpResponseNotFound("<h2>Person no found</h2>")


@login_required
def deletegroup(request, id):
    try:
        dep = Group.objects.get(pk=id)
        dep.delete()
        return redirect('group')
    except Faculty.DoesNotExist:
        return HttpResponseNotFound("<h2>this person not found</h2>")

# Студенты


def student(request):
    search_query = request.GET.get('search', '')
    if search_query:
        student_model = Student.objects.filter(
            student_name__icontains=search_query)
    else:
        student_model = Student.objects.all()

    if request.method == 'GET':
        form = StudentForm()
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_model = form.save(commit=False)
            student_model.student_name = form.cleaned_data['student_name']
            student_model.group_code = form.cleaned_data['group_code']
            student_model.education_type_code = form.cleaned_data['education_type_code']
            student_model.personal_reckoning_number = form.cleaned_data['personal_reckoning_number']
            student_model.bank_code = form.cleaned_data['bank_code']
            student_model.save()
            return redirect('student')
    return render(
        request,
        'main/student.html',
        {
            'form': form,
            'student_model': student_model[::-1]
        }
    )


def showstudent(request, id):
    try:
        post = get_object_or_404(Student, pk=id)
        slaves = Accrual.objects.filter(student_code=id)
        if request.method == 'GET':
            form = StudentForm(instance=post)
        elif request.method == 'POST':
            form = StudentForm(request.POST, instance=post)
            if form.is_valid():
                # post.student_name = form.cleaned_data['student_name']
                # post.group_code = form.cleaned_data['group_code']
                # post.education_type_code = form.cleaned_data['education_type_code']
                # post.personal_reckoning_number = form.cleaned_data['personal_reckoning_number']
                # post.bank_code = form.cleaned_data['bank_code']
                form.save()
                return HttpResponseRedirect(reverse('showstudent', args=(id,)))
        context = {
            'post': post,
            'form': form,
            'slaves': slaves,
        }
        return render(
            request,
            'main/showstudent.html',
            context
        )
    except Staff.DoesNotExist:
        return HttpResponseNotFound("<h2>Person no found</h2>")


@login_required
def deletestudent(request, id):
    try:
        dep = Student.objects.get(pk=id)
        dep.delete()
        return redirect('student')
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>this person not found</h2>")

# Стипендиаты


def fellow(request):
    search_query = request.GET.get('search', '')
    if search_query:
        fellow_model = Fellow.objects.filter(
            student_code_student_name__icontains=search_query)
    else:
        fellow_model = Fellow.objects.all()
    # fellow_model = Fellow.objects.all()
    if request.method == 'GET':
        form = FellowForm()
    elif request.method == 'POST':
        form = FellowForm(request.POST)
        if form.is_valid():
            fellow_model = form.save(commit=False)
            fellow_model.student_code = form.cleaned_data['student_code']
            fellow_model.scholarship_type_code = form.cleaned_data['scholarship_type_code']
            fellow_model.beginning_of_the_accrual_period = form.cleaned_data[
                'beginning_of_the_accrual_period']
            fellow_model.ending_of_the_accrual_period = form.cleaned_data[
                'ending_of_the_accrual_period']
            fellow_model.save()
            return redirect('fellow')
    return render(
        request,
        'main/fellow.html',
        {
            'form': form,
            'fellow_model': fellow_model[::-1]
        }
    )


def showfellow(request, id):
    try:
        post = get_object_or_404(Fellow, pk=id)
        if request.method == 'GET':
            form = FellowForm(instance=post)
        elif request.method == 'POST':
            form = FellowForm(request.POST, instance=post)
            if form.is_valid():
                # post.student_code = form.cleaned_data['student_code']
                # post.scholarship_type_code = form.cleaned_data['scholarship_type_code']
                # post.beginning_of_the_accrual_period = form.cleaned_data['beginning_of_the_accrual_period']
                # post.ending_of_the_accrual_period = form.cleaned_data['ending_of_the_accrual_period']
                form.save()
                return HttpResponseRedirect(reverse('showfellow', args=(id,)))
        context = {
            'post': post,
            'form': form
        }
        return render(
            request,
            'main/showfellow.html',
            context
        )
    except Staff.DoesNotExist:
        return HttpResponseNotFound("<h2>Person no found</h2>")


def deletefellow(request, id):
    try:
        dep = Fellow.objects.get(pk=id)
        dep.delete()
        return redirect('fellow')
    except Faculty.DoesNotExist:
        return HttpResponseNotFound("<h2>this person not found</h2>")

# Начисления


def accrual(request):
    accrual_model = Accrual.objects.all()
    if request.method == 'GET':
        form = AccrualForm()
    elif request.method == 'POST':
        form = AccrualForm(request.POST)
        if form.is_valid():
            accrual_model = form.save(commit=False)
            accrual_model.student_code = form.cleaned_data['student_code']
            accrual_model.date_of_scholarship_accrual = form.cleaned_data[
                'date_of_scholarship_accrual']
            accrual_model.amount_of_money = form.cleaned_data['amount_of_money']
            accrual_model.save()
            return redirect('accrual')
    return render(
        request,
        'main/accrual.html',
        {
            'form': form,
            'accrual_model': accrual_model[::-1]
        }
    )


def showaccrual(request, id):
    try:
        post = get_object_or_404(Accrual, pk=id)
        if request.method == 'GET':
            form = AccrualForm(instance=post)
        elif request.method == 'POST':
            form = AccrualForm(request.POST, instance=post)
            if form.is_valid():
                # post.student_code = form.cleaned_data['student_code']
                # post.date_of_scholarship_accrual = form.cleaned_data['date_of_scholarship_accrual']
                # post.amount_of_money = form.cleaned_data['amount_of_money']
                form.save()
                return HttpResponseRedirect(reverse('showaccrual', args=(id,)))
        context = {
            'post': post,
            'form': form,
        }
        return render(
            request,
            'main/showaccrual.html',
            context
        )
    except Staff.DoesNotExist:
        return HttpResponseNotFound("<h2>Person no found</h2>")


@login_required
def deleteaccrual(request, id):
    try:
        dep = Accrual.objects.get(pk=id)
        dep.delete()
        funds = Scholarship_Fund.objects.all()
        # for fund in funds:
        #     funds.save()
        return redirect('accrual')
    except Faculty.DoesNotExist:
        return HttpResponseNotFound("<h2>this person not found</h2>")

# Сотрудники


@login_required
def editstaff(request, id):
    try:
        staff = Staff.objects.get(pk=id)
        if request.method == "POST":
            staff.curator_name = request.POST.get("name")
            staff.save()
            return redirect('reports')
        else:
            return render(
                request,
                "main/edit.html",
                {"staff": staff}
            )
    except Staff.DoesNotExist:
        return HttpResponseNotFound("<h2>Person no found</h2>")


def reports(request):
    context = modelobjects()

    return render(
        request,
        'main/reports.html',
        context
    )


@login_required
def deletestaff(request, id):
    try:
        staff = Staff.objects.get(pk=id)
        staff.delete()
        return redirect('reports')
    except Staff.DoesNotExist:
        return HttpResponseNotFound("<h2>this person not found</h2>")


def showfund(request, id):
    try:
        context = modelobjects()
        fund = Scholarship_Fund.objects.get(pk=id)
        if request.method == "POST":
            fund.save()
            return redirect('reports')
        else:
            return render(
                request,
                'main/reports.html',
                context
            )
    except Staff.DoesNotExist:
        return HttpResponseNotFound("<h2>Person no found</h2>")

# Авторизация


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('login'))
                else:
                    return HttpResponse('Аккаунт не активен')
            else:
                return HttpResponse('Неправильный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'main/authorization.html', {'form': form})


def get(self, request):
    logout(request)
    return HttpResponseRedirect('/')


def authorization(request):
    return render(
        request,
        'main/authorization.html'
    )
