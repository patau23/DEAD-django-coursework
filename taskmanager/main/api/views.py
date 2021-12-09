from django.db.models import query
from django.http.response import Http404
from rest_framework import viewsets
from django.shortcuts import get_object_or_404, redirect, render

from .serializers import *
from ..models import *


# class ApiViewSet(viewsets.ModelViewSet):
#     queryset =

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class Types_of_EducationViewSet(viewsets.ModelViewSet):
    queryset = Types_of_Education.objects.all()
    serializer_class = Types_of_EducationSerializer


class Types_of_ScholarshipViewSet(viewsets.ModelViewSet):
    queryset = Types_of_Scholarship.objects.all()
    serializer_class = Types_of_ScholarshipSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class AccrualViewSet(viewsets.ModelViewSet):
    queryset = Accrual.objects.all()
    serializer_class = AccrualSerializer


class Scholarship_FundViewSet(viewsets.ModelViewSet):
    queryset = Scholarship_Fund.objects.all()
    serializer_class = Scholarship_FundSerializer


class FellowViewSet(viewsets.ModelViewSet):
    queryset = Fellow.objects.all()
    serializer_class = FellowSerializer


def api_view(request):
    """ there will be  """
    pass


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


def api_review(request):
    context = modelobjects()

    return render(
        request,
        'main/api_review.html',
        context
    )
