from django.db.models import fields
from rest_framework import serializers

from ..models import *


class BankSerializer (serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = '__all__'


class Types_of_EducationSerializer (serializers.ModelSerializer):

    class Meta:
        model = Types_of_Education
        fields = '__all__'


class Types_of_ScholarshipSerializer (serializers.ModelSerializer):

    class Meta:
        model = Types_of_Scholarship
        fields = '__all__'


class StaffSerializer (serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = '__all__'


class FacultySerializer (serializers.ModelSerializer):

    deanery_employee_code_val = serializers.CharField(
        source='deanery_employee_code.curator_name', read_only=True)

    class Meta:
        model = Faculty
        fields = (
            'faculty_code',
            'faculty_name',
            'deanery_employee_code',
            'deanery_employee_code_val'
        )


class DepartmentSerializer (serializers.ModelSerializer):
    faculty_code_val = serializers.CharField(
        source='faculty_code.faculty_name', read_only=True)
    department_head_code_val = serializers.CharField(
        source='department_head_code.curator_name', read_only=True)

    class Meta:
        model = Department
        fields = (
            'department_code',
            'department_name',
            'faculty_code',
            'faculty_code_val',
            'department_head_code',
            'department_head_code_val',
        )


class GroupSerializer (serializers.ModelSerializer):
    issuing_department_code_val = serializers.CharField(
        source='issuing_department_code.department_name', read_only=True)
    сurator_code_val = serializers.CharField(
        source='сurator_code.curator_name', read_only=True)

    class Meta:
        model = Group
        fields = (
            'group_code',
            'group_name',
            'issuing_department_code',
            'issuing_department_code_val',
            'сurator_code',
            'сurator_code_val',
        )


class StudentSerializer (serializers.ModelSerializer):
    group_code_val = serializers.CharField(
        source='group_code.group_name', read_only=True)
    education_type_code_val = serializers.CharField(
        source='education_type_code.education_type_name', read_only=True)
    bank_code_val = serializers.CharField(
        source='bank_code.bank_name', read_only=True)

    class Meta:
        model = Student
        fields = (
            'student_code',
            'student_name',
            'group_code',
            'group_code_val',
            'education_type_code',
            'education_type_code_val',
            'personal_reckoning_number',
            'bank_code',
            'bank_code_val',
        )


class AccrualSerializer (serializers.ModelSerializer):
    student_code_val = serializers.CharField(
        source='student_code.student_name', read_only=True)

    class Meta:
        model = Accrual
        fields = (
            'id',
            'student_code',
            'student_code_val',
            'date_of_scholarship_accrual',
            'amount_of_money',
        )


class Scholarship_FundSerializer (serializers.ModelSerializer):
    faculty_code_val = serializers.CharField(
        source='faculty_code.faculty_name', read_only=True)

    class Meta:
        model = Scholarship_Fund
        fields = (
            'faculty_code',
            'faculty_code_val',
            'scholarship_amount',
        )


class FellowSerializer (serializers.ModelSerializer):
    student_code_val = serializers.CharField(
        source='student_code.student_name', read_only=True)
    scholarship_type_code_val = serializers.CharField(
        source='scholarship_type_code.scholarship_type_name', read_only=True)

    class Meta:
        model = Fellow
        fields = (
            'student_code',
            'student_code_val',
            'scholarship_type_code',
            'scholarship_type_code_val',
            'beginning_of_the_accrual_period',
            'ending_of_the_accrual_period',
        )
