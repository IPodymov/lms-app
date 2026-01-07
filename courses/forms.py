from django import forms
from .models import AuthorApplication, Course


class AuthorApplicationForm(forms.ModelForm):
    class Meta:
        model = AuthorApplication
        fields = ["message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4, "placeholder": "Расскажите о себе..."}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "cover"]
