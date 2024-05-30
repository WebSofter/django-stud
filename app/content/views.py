from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import (
    DetailView,
    ListView,
)

from .forms import ContentFormCreation, ContentFormUpdation

# from forms import ContentFormCreation
from .models import Category, Content

def ContentViewList(request):
  '''вывод записей'''
  contents = []
  if request.user.is_superuser:
    contents = Content.objects.all
  else:
    contents = Content.objects.filter(user_id=request.user.id)
    
  categories = Category.objects.all
  return render(request, 'content_list.html', { 'segment': 'content', 'contents': contents, 'categories': categories, })


class ContentViewCreation(LoginRequiredMixin, View):
    template_name = 'content_create.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context["form"] = ContentFormCreation()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form_creation = ContentFormCreation(request.POST, request.FILES)
        if form_creation.is_valid():
            content = form_creation.save(commit=False)
            content.user = request.user
            content.save()
            form_creation.save_m2m()

            messages.success(self.request, f"Пост удачно опубликован.")
            return redirect(to="content_detail", slug=content.slug)

        self.context["form"] = form_creation
        #messages.error(request, "Пожалуйста, заполните все неоходимые поля")
        return render(request, self.template_name, self.context)

class ContentViewUpdation(LoginRequiredMixin, View):

    template_name = 'content_update.html'
    context_object = {}

    def get(self, request, *args, **kwargs):

        content = get_object_or_404(Content, slug=self.kwargs.get("slug"))
        form = ContentFormUpdation(instance=content,)
        return render(request, self.template_name, {'content': content, 'form': form})

    def post(self, request, *args, **kwargs):
        old_content = get_object_or_404(Content, slug=self.kwargs.get("slug"))
        content_update_form = ContentFormCreation(request.POST, request.FILES, instance=old_content)
        if content_update_form.is_valid():

            content = content_update_form.save(commit=False)
            content.user = request.user
            content.date_created = timezone.now()
            content.date_updated = timezone.now()
            content.save()
            content_update_form.save_m2m()

            messages.success(self.request, f"Пост обновлен удачно.")
            return redirect(to="content_detail", slug=content.slug)

        self.context_object["content"] = content_update_form
        #messages.error(request, "Пожалуйста, заполните все необходимые поля")
        return render(request, self.template_name, self.context_object)

class ContentViewDetail(DetailView):
    model = Content
    template_name = 'content_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['related_contents'] = Content.objects.filter(category=self.object.category,).order_by('?')[:3]
        kwargs['content'] = self.object
        return super().get_context_data(**kwargs)