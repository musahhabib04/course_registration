from django import forms
from .models import Course
from .models import Enrollment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title']
        

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
