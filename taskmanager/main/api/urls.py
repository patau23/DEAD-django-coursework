from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from .views import *


router = routers.SimpleRouter()
router.register('bank', BankViewSet, basename='bank')
router.register('educ-type', Types_of_EducationViewSet, basename='educ-type')
router.register('scholar-type', Types_of_ScholarshipViewSet, basename='scholar-type')
router.register('staff', StaffViewSet, basename='staff')
router.register('faculty', FacultyViewSet, basename='faculty')
router.register('department', DepartmentViewSet, basename='department')
router.register('group', GroupViewSet, basename='group')
router.register('student', StudentViewSet, basename='student')
router.register('accrual', AccrualViewSet, basename='accrual')
router.register('scholar-fund', Scholarship_FundViewSet, basename='scholar-fund')
router.register('fellow', FellowViewSet, basename='fellow')

urlpatterns = [
    path('', api_review),
    path('api-view/', api_view)
]
urlpatterns += router.urls