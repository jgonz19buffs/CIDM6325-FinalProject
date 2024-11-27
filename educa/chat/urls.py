from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name  = 'chat'

urlpatterns = [
    path(
        _('room/<int:course_id>/'),
        views.course_chat_room,
        name='course_chat_room'),
]