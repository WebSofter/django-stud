from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import (
    DetailView,
)
from .forms import CourseFormCreation, CourseFormUpdation
from .models import Category, Course

class CourseViewList(LoginRequiredMixin, View):
    template_name = 'course_create.html'
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all
        categories = Category.objects.all
        return render(request, self.template_name, {'segment': 'course', 'courses': courses, 'categories': categories, })


class CourseViewCreation(LoginRequiredMixin, View):
    template_name = 'course_create.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context["form"] = CourseFormCreation()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form_creation = CourseFormCreation(request.POST, request.FILES)
        if form_creation.is_valid():
            course = form_creation.save(commit=False)
            course.user = request.user
            course.save()
            form_creation.save_m2m()

            messages.success(self.request, f"Пост удачно опубликован.")
            return redirect(to="course_detail", slug=course.slug)

        self.context["form"] = form_creation
        messages.error(request, "Пожалуйста, заполните все неоходимые поля")
        return render(request, self.template_name, self.context)


class CourseViewUpdation(LoginRequiredMixin, View):

    template_name = 'course_update.html'
    context_object = {}

    def get(self, request, *args, **kwargs):

        course = get_object_or_404(Course, slug=self.kwargs.get("slug"))
        form = CourseFormUpdation(instance=course,)
        return render(request, self.template_name, {'course': course, 'form': form})

    def post(self, request, *args, **kwargs):
        old_course = get_object_or_404(Course, slug=self.kwargs.get("slug"))
        course_update_form = CourseFormCreation(
            request.POST, request.FILES, instance=old_course)
        if course_update_form.is_valid():

            course = course_update_form.save(commit=False)
            course.user = request.user
            course.date_created = timezone.now()
            course.date_updated = timezone.now()
            course.save()
            course_update_form.save_m2m()

            messages.success(self.request, f"Пост обновлен удачно.")
            return redirect(to="course:course_detail", slug=course.slug)

        self.context_object["course"] = course_update_form
        messages.error(request, "Пожалуйста, заполните все необходимые поля")
        return render(request, self.template_name, self.context_object)


class CourseViewDetail(DetailView):
    model = Course
    template_name = 'course_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['related_courses'] = Course.objects.filter(
            category=self.object.category,).order_by('?')[:3]
        kwargs['course'] = self.object
        return super().get_context_data(**kwargs)
