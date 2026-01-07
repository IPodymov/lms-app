from django.urls import path
from .views import (
    CourseListView,
    AuthorApplicationCreateView,
    CourseCreateView,
    CourseDetailView,
    CourseEditView,
    EnrollCourseView,
    ChapterCreateView,
    ChapterUpdateView,
    ChapterDeleteView,
)

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path("course/<int:pk>/edit/", CourseEditView.as_view(), name="course_edit"),
    path("course/<int:pk>/enroll/", EnrollCourseView.as_view(), name="enroll_course"),
    path(
        "course/<int:course_pk>/chapter/add/",
        ChapterCreateView.as_view(),
        name="chapter_create",
    ),
    path(
        "chapter/<int:pk>/edit/",
        ChapterUpdateView.as_view(),
        name="chapter_edit",
    ),
    path(
        "chapter/<int:pk>/delete/",
        ChapterDeleteView.as_view(),
        name="chapter_delete",
    ),
    path("apply-author/", AuthorApplicationCreateView.as_view(), name="apply_author"),
    path("create-course/", CourseCreateView.as_view(), name="create_course"),
]
