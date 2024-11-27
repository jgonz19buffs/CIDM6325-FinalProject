from django.urls import path
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path(
        _('content/order/'),
        views.ContentOrderView.as_view(),
        name='content_order'
    ),
    path(
        _('courses/'),
        views.StudentCourseListView.as_view(),
        name='student_course_list'
    ),
    path(
        _('course/<pk>/work/content/<model_name>/create/'),
        views.WorkContentCreateUpdateView.as_view(),
        name='work_content_create'
    ), 
    path(
        _('course/<pk>/work/content/<model_name>/<id>/'),
        views.WorkContentCreateUpdateView.as_view(),
        name='work_content_update'
    ),
    path(
        _('course/<pk>/work/<work_id>/'),
        cache_page(60 * 15)(views.StudentCourseWorkDetailView.as_view()),
        name='student_work_detail'
    ),
    path(
        _('course/<pk>/work/'),
        cache_page(60 * 15)(views.StudentCourseWorkListView.as_view()),
        name='student_work_list'
    ),
    path(
        _('course/<pk>/'),
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail'
    ),
    path(
        _('course/<pk>/<module_id>/'),
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail_module'
    ),

    path(
        _('enroll-course'),
        views.StudentEnrollCourseView.as_view(),
        name='student_enroll_course'
        ),
    path(
        _('register/'),
        views.StudentRegistrationView.as_view(),
        name='student_registration'
    ),
]
