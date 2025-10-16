from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import Course, Enrollment
from .forms import CourseForm
from django.contrib.auth import login
from .forms import SignUpForm

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.tutor = request.user
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})

@login_required(login_url='/accounts/login/')
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})


def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment, created = Enrollment.objects.get_or_create(student=request.user, course=course)

    if not created:
        messages.warning(request, "You are already enrolled in this course.")
    else:
        messages.success(request, f"You have successfully enrolled in {course.title}.")
    return redirect('my_courses')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the new user automatically
            return redirect('course_list')  # redirect to a page (like the course list)
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
