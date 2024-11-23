from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	"""Форма регистрации нового пользователя.

	Атрибуты:
			email (EmailField): Поле для ввода адреса электронной почты.

	Методы:
			Meta: Определяет модель и поля для формы.
	"""
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	"""Форма для обновления данных пользователя.

	Атрибуты:
			email (EmailField): Поле для ввода адреса электронной почты.

	Методы:
			Meta: Определяет модель и поля для формы.
	"""
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	"""Форма для обновления профиля пользователя.

	Методы:
			Meta: Определяет модель и поля для формы.
	"""

	class Meta:
		model = Profile
		fields = ['image']
