from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import Course, AuthorApplication, Chapter
from .forms import AuthorApplicationForm, CourseForm, ChapterForm


class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"

    def get_queryset(self):
        return Course.objects.filter(status="published")


class AuthorApplicationCreateView(LoginRequiredMixin, CreateView):
    model = AuthorApplication
    form_class = AuthorApplicationForm
    template_name = "courses/apply_author.html"
    success_url = reverse_lazy("course_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CourseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/create_course.html"
    success_url = reverse_lazy("course_list")

    def test_func(self):
        return self.request.user.is_author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["is_enrolled"] = self.object.students.filter(
                id=self.request.user.id
            ).exists()
        else:
            context["is_enrolled"] = False
        return context


class EnrollCourseView(LoginRequiredMixin, View):
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return redirect("course_detail", pk=pk)


class CourseEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/edit_course.html"

    def test_func(self):
        course = self.get_object()
        return self.request.user == course.author

    def get_success_url(self):
        return reverse("course_detail", kwargs={"pk": self.object.pk})


class ChapterCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Chapter
    form_class = ChapterForm
    template_name = "courses/chapter_form.html"

    def test_func(self):
        course = get_object_or_404(Course, pk=self.kwargs["course_pk"])
        return self.request.user == course.author

    def form_valid(self, form):
        form.instance.course = get_object_or_404(Course, pk=self.kwargs["course_pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = get_object_or_404(Course, pk=self.kwargs["course_pk"])
        context["action"] = "Добавить"
        return context

    def get_success_url(self):
        return reverse("course_detail", kwargs={"pk": self.kwargs["course_pk"]})


class ChapterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chapter
    form_class = ChapterForm
    template_name = "courses/chapter_form.html"

    def test_func(self):
        chapter = self.get_object()
        return self.request.user == chapter.course.author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = self.object.course
        context["action"] = "Редактировать"
        return context

    def get_success_url(self):
        return reverse("course_detail", kwargs={"pk": self.object.course.pk})


class ChapterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chapter
    template_name = "courses/chapter_confirm_delete.html"

    def test_func(self):
        chapter = self.get_object()
        return self.request.user == chapter.course.author

    def get_success_url(self):
        return reverse("course_detail", kwargs={"pk": self.object.course.pk})
