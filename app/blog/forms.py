from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django import forms
from .models import Category, Post
from django.utils.translation import gettext_lazy as _

class PostFormBase(forms.ModelForm):
    title = forms.CharField(
        label=_("Заголовок"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
    )
    # category = forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категория'},)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), #filter(approved=True),
                                      empty_label="Выбрать категорию",
                                      widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категория'},)
                                    )
    image = forms.ImageField()
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Заголовок', 'rows': 3}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
       print(self)
        # post = super().save(commit=False)
        # if commit:
        #     post.save()
        # return post

class PostFormCreation(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), #filter(approved=True),
                                      empty_label="Выбрать категорию",
                                      widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категория'},)
                                    )

    class Meta:
        # Статусы постов
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # Выборка
        STATUS_CHOICES = (
            (DRAFTED, 'Черновик'),
            (PUBLISHED, 'Опубликован'),
        )
        
        model = Post
        fields = ('title', 'category', 'image', 'text', 'status')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фотография',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст',
            }),
            'status': forms.Select(choices=STATUS_CHOICES, attrs={
                'class': 'form-control',
                'placeholder': 'Категория',
            }),
        }

class PostFormUpdation(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), #filter(approved=True),
                                      empty_label="Выбрать категорию",
                                      widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категория'},)
                                    )

    class Meta:
        # Статусы постов
        DRAFTED = "DRAFTED"
        PUBLISHED = "PUBLISHED"

        # Выборка
        STATUS_CHOICES = (
            (DRAFTED, 'Черновик'),
            (PUBLISHED, 'Опубликован'),
        )
        
        model = Post
        fields = ('title', 'category', 'image', 'text', 'status')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фотография',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст',
            }),
            'status': forms.Select(choices=STATUS_CHOICES, attrs={
                'class': 'form-control',
                'placeholder': 'Категория',
            }),
        }