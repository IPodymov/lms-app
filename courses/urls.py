from django.urls import path
from .views import (
    CourseListView,
    AuthorApplicationCreateView,
    CourseCreateView,
    CourseDetailView,
    EnrollCourseView,
)

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path("course/<int:pk>/enroll/", EnrollCourseView.as_view(), name="enroll_course"),
    path("apply-author/", AuthorApplicationCreateView.as_view(), name="apply_author"),
    path("create-course/", CourseCreateView.as_view(), name="create_course"),
]
