from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django import forms
from .models import Course
from content.models import Category, Content
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.widgets import CKEditor5Widget

class CourseFormCreation(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=Category.objects.all(), #filter(approved=True),
                                      empty_label="Выбрать категорию",
                                      widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категория'},)
                                    )
    class CustomMMCF(forms.ModelMultipleChoiceField):
        def label_from_instance(self, content):
            return f"{content.type} - {content.title}"

    content = CustomMMCF(
        queryset= Content.objects.all(), #get(id=id),
        widget=forms.CheckboxSelectMultiple
        # widget=FilteredSelectMultiple("verbose name", is_stacked=False)
    )
    class Meta:
        
        model = Course
        fields = ('title', 'category', 'image', 'text', 'price')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория',
            }),
            'content': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Контент',
                'title': 'Контент курса',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фотография',
                'title': 'Фото контента',
            }),
            'text': CKEditor5Widget(
                attrs={
                    'class': "form-control django_ckeditor_5",
                    'placeholder': 'Текст',
                },
                config_name="extends",
            ),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Стоимость',}),
        }
    
    def __init__(self, *args, **kwargs):
        #self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        #self.fields['content'].queryset = Content.objects.filter(user=self.request.user)
        self.fields["text"].required = False
        

class CourseFormUpdation(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), #filter(approved=True),
                                      empty_label="Выбрать категорию",
                                      widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категория'},)
                                    )
    class CustomMMCF(forms.ModelMultipleChoiceField):
        def label_from_instance(self, content):
            return f"{content.type} - {content.title}"
    class Meta:
        
        model = Course
        fields = ('title', 'category', 'image', 'text', 'price')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория',
            }),
            'content': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Контент',
                'title': 'Контент курса',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фотография',
                'title': 'Фото контента',
            }),
            'text': CKEditor5Widget(
                attrs={
                    'class': "form-control django_ckeditor_5",
                    'placeholder': 'Текст',
                },
                config_name="extends",
            ),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Стоимость',}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False
