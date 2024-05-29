from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import (
    DetailView,
    ListView,
)

from .forms import AnalysisFormCreation, AnalysisFormUpdation

# from forms import AnalysisFormCreation
from .models import Analysis

def AnalysisViewList(request):
  '''вывод записей'''
  analysis = []
  if request.user.is_superuser:
    analysis = Analysis.objects.all
  else:
    analysis = Analysis.objects.filter(user_id=request.user.id)
  return render(request, 'analysis_list.html', { 'segment': 'analysis', 'analysis': analysis,})


class AnalysisViewCreation(LoginRequiredMixin, View):
    template_name = 'analysis_create.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context["form"] = AnalysisFormCreation()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form_creation = AnalysisFormCreation(request.POST, request.FILES)
        if form_creation.is_valid():
            analysis = form_creation.save(commit=False)
            analysis.user = request.user
            analysis.save()
            form_creation.save_m2m()

            messages.success(self.request, f"Анализ удачно опубликован.")
            return redirect(to="analysis")

        self.context["form"] = form_creation
        messages.error(request, "Пожалуйста, заполните все неоходимые поля")
        return render(request, self.template_name, self.context)

class AnalysisViewUpdation(LoginRequiredMixin, View):

    template_name = 'analysis_update.html'
    context_object = {}

    def get(self, request, *args, **kwargs):

        old_analysis = get_object_or_404(Analysis, id=self.kwargs.get("id"))
        form = AnalysisFormUpdation(instance=old_analysis, )

        self.context_object["form"] = form
        self.context_object["analysis"] = old_analysis
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):

        old_analysis = get_object_or_404(Analysis, id=self.kwargs.get("id"))
        form = AnalysisFormCreation(request.POST, request.FILES, instance=old_analysis)
        if form.is_valid():

            analysis = form.save(commit=False)
            analysis.author = request.user
            analysis.date_created = timezone.now()
            analysis.save()
            form.save_m2m()

            messages.success(self.request, f"Анализ обновлен удачно.")
            return redirect(to="analysis:analysis_detail", id=analysis.id)

        self.context_object["analysis"] = form
        messages.error(request, "Пожалуйста, заполните все необходимые поля")
        return render(request, self.template_name, self.context_object)

class AnalysisViewDetail(DetailView):
    model = Analysis
    template_name = 'analysis_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['analysis'] = self.object
        return super().get_context_data(**kwargs)