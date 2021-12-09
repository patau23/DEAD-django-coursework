from django.contrib import admin
from .models import *


# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    list_display = (
        'faculty_name', 
        'deanery_employee_code',
        'faculty_code', )
admin.site.register(Faculty, FacultyAdmin)



class FellowsAdmin(admin.ModelAdmin):
    list_display = (
        'student_code', 
        'scholarship_type_code', 
        'beginning_of_the_accrual_period',
        'ending_of_the_accrual_period')
admin.site.register(Fellow, FellowsAdmin)



class BankAdmin(admin.ModelAdmin):
    list_display = (
        'bank_name',
        'bank_code',) 
admin.site.register(Bank, BankAdmin)



class AccrualsAdmin(admin.ModelAdmin):
    list_display = (
        'student_code', 
        'date_of_scholarship_accrual', 
        'amount_of_money')
admin.site.register(Accrual, AccrualsAdmin)



class StudentsAdmin(admin.ModelAdmin):
    list_display = (
        'student_code', 
        'student_name', 
        'group_code', 
        'education_type_code', 
        'personal_reckoning_number', 
        'bank_code')
admin.site.register(Student, StudentsAdmin)



class Types_of_ScholarshipsAdmin(admin.ModelAdmin):
    list_display = (
        'scholarship_type_name', 
        'scholarship_type_code', 
        'amount_of_money')
admin.site.register(Types_of_Scholarship, Types_of_ScholarshipsAdmin)



class Types_of_EducationAdmin(admin.ModelAdmin):
    list_display = (
        'education_type_name',
        'education_type_code',) 
admin.site.register(Types_of_Education, Types_of_EducationAdmin)



class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'group_name', 
        'group_code', 
        'issuing_department_code', 
        'сurator_code')
admin.site.register(Group, GroupAdmin)



class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'department_name', 
        'department_code', 
        'faculty_code', 
        'department_head_code')
admin.site.register(Department, DepartmentAdmin)



class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'curator_name',
        'сurator_code',) 
admin.site.register(Staff, StaffAdmin)



class Scholarship_FundAdmin(admin.ModelAdmin):
    list_display = (
        'faculty_code', 
        'scholarship_amount')
admin.site.register(Scholarship_Fund, Scholarship_FundAdmin)
