from django.contrib import admin
from .models import Course, AuthorApplication, Chapter


@admin.action(description="Одобрить выбранные заявки")
def approve_applications(modeladmin, request, queryset):
    for app in queryset:
        app.status = "approved"
        app.save()
        # Выдаем права автора
        app.user.is_author = True
        app.user.save()


@admin.action(description="Отклонить выбранные заявки")
def reject_applications(modeladmin, request, queryset):
    queryset.update(status="rejected")


@admin.register(AuthorApplication)
class AuthorApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "status", "created_at")
    list_filter = ("status", "created_at")
    actions = [approve_applications, reject_applications]


@admin.action(description="Опубликовать выбранные курсы")
def publish_courses(modeladmin, request, queryset):
    queryset.update(status="published")


class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("title", "description")
    actions = [publish_courses]
    inlines = [ChapterInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def has_change_permission(self, request, obj=None):
        if not obj:
            return super().has_change_permission(request, obj)
        return obj.author == request.user or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        if not obj:
            return super().has_delete_permission(request, obj)
        return obj.author == request.user or request.user.is_superuser
