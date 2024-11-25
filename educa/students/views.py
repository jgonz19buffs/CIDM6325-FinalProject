from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from django.apps import apps
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.forms.models import modelform_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from .forms import CourseEnrollForm
from courses.models import Content, Course, Work
from urllib.parse import urlparse
import os

# Create your views here.
class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(
            username=cd['username'], password=cd['password1']
        )
        login(self.request, user)
        return result

class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy(
            'student_course_detail', args=[self.course.id]
        )

class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])
    
class StudentCourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get course object
        course = self.get_object()
        if 'module_id' in self.kwargs:
            # get current module
            context['module'] = course.modules.get(
                id=self.kwargs['module_id']
            )
        else:
            # get first module
            context['module'] = course.modules.all()[0]
        return context

class StudentCourseWorkListView(LoginRequiredMixin, ListView):
    model = Work
    template_name = 'students/course/work/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user.id, course_id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_id'] = self.kwargs['pk']
        return context

class StudentCourseWorkDetailView(LoginRequiredMixin, ListView):
    model = Work
    template_name = 'students/course/work/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_id'] = self.kwargs['pk']
        # get work object
        work = self.get_object()
        if 'work_id' in self.kwargs:
            # get current work
            context['work'] = work.get(
                id=self.kwargs['work_id']
            )
        else:
            # get first work
            context['work'] = work.all()[0]
        return context

class WorkContentCreateUpdateView(TemplateResponseMixin, View):
    work = None
    model = None
    obj = None
    template_name = 'courses/work/form.html'

    def get_model(self, model_name):
        if model_name in ['text', 'video', 'image', 'file']:
            return apps.get_model(
                app_label='courses', model_name=model_name
            )
        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(
            model, exclude=['owner', 'order', 'created', 'updated']
        )
        return Form(*args, **kwargs)

    def dispatch(self, request, pk, model_name, id=None):
        self.course = get_object_or_404(
            Course, id=pk
        )
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(
                self.model, id=id, owner=request.user
            )
        return super().dispatch(request, pk, model_name, id)

    def get(self, request, work_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response(
            {'form': form, 'object': self.obj}
        )

    def post(self, request, pk, model_name, id=None):
        form = self.get_form(
            self.model,
            instance=self.obj,
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user

            file = request.FILES.get('file')
            url = request.POST.get('url')
            if(file):
                if(model_name == 'image'):
                    file_extension = os.path.splitext(file.name)[1].lower()
                    if file_extension != '.png':
                        form.add_error('file', 'Invalid file type')
                        return self.render_to_response({'form':form, 'object':self.obj})
                
                if(model_name == 'file'):
                    file_extension = os.path.splitext(file.name)[1].lower()
                    if file_extension != '.pdf':
                        form.add_error('file', 'Invalid file type')
                        return self.render_to_response({'form':form, 'object':self.obj})
                
                if(model_name == 'video'):
                    file_extension = os.path.splitext(file.name)[1].lower()
                    if file_extension != '.mp4':
                        form.add_error('file', 'Invalid file type')
                        return self.render_to_response({'form':form, 'object':self.obj})

            obj.save()
            if not id:
                # new content
                Work.objects.create(course = self.course, item=obj, owner = request.user, title = obj.title)
            return redirect('student_work_list', self.course.id)
        return self.render_to_response(
            {'form': form, 'object': self.obj}
        )
    
class ContentOrderView(CsrfExemptMixin, JsonRequestResponseMixin, View):
    def post(self, request):
        for id, order in self.request_json.items():
            Content.objects.filter(
                id=id, module__course__owner=request.user
            ).update(order=order)
        return self.render_json_response({'saved': 'OK'})