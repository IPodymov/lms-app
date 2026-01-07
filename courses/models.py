from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from cloudinary.models import CloudinaryField

User = get_user_model()


class AuthorApplication(models.Model):
    STATUS_CHOICES = (
        ("pending", "На рассмотрении"),
        ("approved", "Одобрено"),
        ("rejected", "Отклонено"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author_applications",
        verbose_name="Пользователь",
    )
    message = models.TextField(
        verbose_name="Сообщение / Опыт работы",
        help_text="Почему вы хотите стать автором?",
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="Статус"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Заявка от {self.user.username} - {self.get_status_display()}"

    class Meta:
        verbose_name = "Заявка на авторство"
        verbose_name_plural = "Заявки на авторство"


class Course(models.Model):
    STATUS_CHOICES = (
        ("draft", "Черновик"),
        ("moderation", "На модерации"),
        ("published", "Опубликован"),
    )

    title = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание")
    cover = CloudinaryField("image", folder="course_covers/", blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="Автор",
    )
    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="enrolled_courses",
        blank=True,
        verbose_name="Студенты",
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="draft", verbose_name="Статус"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Chapter(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="chapters", verbose_name="Курс"
    )
    title = models.CharField(max_length=200, verbose_name="Название главы")
    description = models.TextField(verbose_name="Описание", blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Порядковый номер")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Глава"
        verbose_name_plural = "Главы"
        ordering = ["order", "created_at"]

    def __str__(self):
        return f"{self.course.title} - {self.title}"
