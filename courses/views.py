from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Course, AuthorApplication
from .forms import AuthorApplicationForm, CourseForm

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.filter(status='published')

class AuthorApplicationCreateView(LoginRequiredMixin, CreateView):
    model = AuthorApplication
    form_class = AuthorApplicationForm
    template_name = 'courses/apply_author.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CourseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/create_course.html'
    success_url = reverse_lazy('course_list')

    def test_func(self):
        return self.request.user.is_author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['is_enrolled'] = self.object.students.filter(id=self.request.user.id).exists()
        else:
            context['is_enrolled'] = False
        return context

class EnrollCourseView(LoginRequiredMixin, View):
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return redirect('course_detail', pk=pk)

