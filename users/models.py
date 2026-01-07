from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    """
    Кастомная модель пользователя.
    Пользователь может быть одновременно и студентом, и автором.
    """

    is_student = models.BooleanField(default=True, verbose_name="Студент")
    is_author = models.BooleanField(default=False, verbose_name="Автор курсов")
    avatar = CloudinaryField('avatar', folder='avatars/', blank=True, null=True)

    def __str__(self):

        return self.username
