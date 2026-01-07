from django import forms
from .models import AuthorApplication, Course, Chapter


class AuthorApplicationForm(forms.ModelForm):
    class Meta:
        model = AuthorApplication
        fields = ["message"]
        widgets = {
            "message": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Расскажите о себе..."}
            ),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "cover"]


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ["title", "description", "order"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 5}
            ),
            "order": forms.NumberInput(attrs={"class": "form-control"}),
        }
