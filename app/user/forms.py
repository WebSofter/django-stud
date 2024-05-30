from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django import forms
from .models import Profile, Role
from django.utils.translation import gettext_lazy as _
from django. contrib.auth.admin import User

class ProfileFormUpdation(forms.ModelForm):
    role = forms.ModelChoiceField(queryset=Role.objects.all(),
                                      empty_label="Выбрать роль",
                                      widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Категория'},)
                                    )
    class Meta:
        # Пол
        MALE = "M"
        FEMALE = "F"

        # Выборка
        GENDER_CHOICES = (
            (MALE, 'Мужской'),
            (FEMALE, 'Женский'),
        )

        model = Profile
        fields = ('photo', 'role', 'gender', 'birth_date', 'balance', 'tg_chat', 'tg_token')

        widgets = {
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фотография',
                'title': 'Фото пользователя',
            }),
            'role': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Роль',
            }),
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={
                'class': 'form-control',
                'placeholder': 'Пол',
            }),
            'birth_date': forms.SelectDateWidget(years=range(1900, 2024), attrs={'class': 'form-control', 'placeholder': 'Дата рождения',}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Баланс',}),
            'tg_chat': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ИД ТГ-чата',
            }),
            'tg_token': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Токен ТГ-чата',
            }),
        }

class UserFormUpdation(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }),
        }


class RoleFormBase(forms.ModelForm):
    class Meta:
        model = Role
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
            }),
        }