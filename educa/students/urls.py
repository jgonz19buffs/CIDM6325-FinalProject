from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path(
        'courses/',
        views.StudentCourseListView.as_view(),
        name='student_course_list'
    ),
    path(
        'course/<pk>/work/',
        cache_page(60 * 15)(views.StudentCourseWorkListView.as_view()),
        name='student_work_list'
    ),
    path(
        'course/<pk>/',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail'
    ),
    path(
        'course/<pk>/<module_id>/',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail_module'
    ),
        path(
        'course/<pk>/work/<work_id>/',
        cache_page(60 * 15)(views.StudentCourseWorkDetailView.as_view()),
        name='student_work_detail'
    ),
    path(
        'enroll-course',
        views.StudentEnrollCourseView.as_view(),
        name='student_enroll_course'
        ),
    path(
        'register/',
        views.StudentRegistrationView.as_view(),
        name='student_registration'
    ),
]