from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django import forms
from .models import Analysis
from django.utils.translation import gettext_lazy as _

class AnalysisFormCreation(forms.ModelForm):

    class Meta:
        
        model = Analysis
        fields = ('weight', 'girth', 'pulse', 'calories_pd', 'steps_pd', )
        widgets = {
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вес',
            }),
            'girth': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Обхват',
            }),
            'pulse': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пульс',
            }),
            'calories_pd': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Набор колорий в день',
            }),
            'steps_pd': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Набор шагов в день',
            }),
        }

class AnalysisFormUpdation(forms.ModelForm):

    class Meta:
        model = Analysis
        fields = ('weight', 'girth', 'pulse', 'calories_pd', 'steps_pd', )

        widgets = {
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вес',
            }),
            'girth': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Обхват',
            }),
            'pulse': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пульс',
            }),
            'calories_pd': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Набор колорий в день',
            }),
            'steps_pd': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Набор шагов в день',
            }),
        }