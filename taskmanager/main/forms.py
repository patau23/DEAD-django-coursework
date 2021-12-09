from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import ModelForm

from .models import *


class BankForm(ModelForm): # банк
    class Meta:
        model = Bank
        fields = '__all__'

class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        
class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class FellowForm(ModelForm):
    class Meta:
        model = Fellow
        fields = '__all__'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['student_code'].queryset = Student.objects.filter(education_type_code = 1)


class AccrualForm(ModelForm):
    class Meta:
        model = Accrual
        fields = '__all__'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['student_code'].queryset = Student.objects.filter(education_type_code = 1)


class Scholarship_FundForm(ModelForm):
    class Meta:
        model = Scholarship_Fund
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
