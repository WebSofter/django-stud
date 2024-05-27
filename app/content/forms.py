from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django import forms
from .models import Category, Content
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.widgets import CKEditor5Widget

class ContentFormCreation(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), #filter(approved=True),
                                      empty_label="Выбрать категорию",
                                      widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категория'},)
                                    )
    class Meta:
        # Тип контента
        RECIPE = "RECIPE"
        IMAGE = "IMAGE"
        FILE = "FILE"
        VIDEO = "VIDEO"
        MENU = "MENU"
        ANALYSIS = "ANALYSIS"
        # Выборка
        TYPE_CHOICES = (
            (RECIPE, 'Рецепт'),
            (IMAGE, 'Изображение'),
            (FILE, 'Файл'),
            (VIDEO, 'Видео'),
            (MENU, 'Меню'),
            (ANALYSIS, 'Анализ'),
        )
        
        model = Content
        fields = ('title', 'category', 'image', 'file', 'text', 'type')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория',
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Файл',
                'title': 'Файл контента',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фотография',
                'title': 'Фото контента',
            }),
            # 'text': forms.Textarea(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Текст',
            # }),
            'text': CKEditor5Widget(
                attrs={
                    'class': "form-control django_ckeditor_5",
                    'placeholder': 'Текст',
                },
                config_name="extends",
            ),
            'type': forms.Select(choices=TYPE_CHOICES, attrs={
                'class': 'form-control',
                'placeholder': 'Категория',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False


class ContentFormUpdation(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), #filter(approved=True),
                                      empty_label="Выбрать категорию",
                                      widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категория'},)
                                    )

    class Meta:
        # Тип контента
        RECIPE = "RECIPE"
        IMAGE = "IMAGE"
        FILE = "FILE"
        VIDEO = "VIDEO"
        MENU = "MENU"
        ANALYSIS = "ANALYSIS"
        # Выборка
        TYPE_CHOICES = (
            (RECIPE, 'Рецепт'),
            (IMAGE, 'Изображение'),
            (FILE, 'Файл'),
            (VIDEO, 'Видео'),
            (MENU, 'Меню'),
            (ANALYSIS, 'Анализ'),
        )
        
        model = Content
        fields = ('title', 'category', 'image', 'file', 'text', 'type')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория',
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Файл',
                'title': 'Файл контента',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фотография',
                'title': 'Фото контента',
            }),
            # 'text': forms.Textarea(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Текст',
            # }),
            'text': CKEditor5Widget(
                attrs={
                    'class': "form-control django_ckeditor_5",
                    'placeholder': 'Текст',
                },
                config_name="extends",
            ),
            'type': forms.Select(choices=TYPE_CHOICES, attrs={
                'class': 'form-control',
                'placeholder': 'Категория',
            }),
        }