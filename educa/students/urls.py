from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path(
        'content/order/',
        views.ContentOrderView.as_view(),
        name='content_order'
    ),
    path(
        'courses/',
        views.StudentCourseListView.as_view(),
        name='student_course_list'
    ),
    path(
        'course/<pk>/work/content/<model_name>/create/',
        views.WorkContentCreateUpdateView.as_view(),
        name='work_content_create'
    ), 
    path(
        'course/<pk>/work/content/<model_name>/<id>/',
        views.WorkContentCreateUpdateView.as_view(),
        name='work_content_update'
    ), 
    path(
        'course/<pk>/work/',
        (views.StudentCourseWorkListView.as_view()),
        name='student_work_list'
    ),
    path(
        'course/<pk>/',
        (views.StudentCourseDetailView.as_view()),
        name='student_course_detail'
    ),
    path(
        'course/<pk>/<module_id>/',
        (views.StudentCourseDetailView.as_view()),
        name='student_course_detail_module'
    ),
        path(
        'course/<pk>/work/<work_id>/',
        (views.StudentCourseWorkDetailView.as_view()),
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
