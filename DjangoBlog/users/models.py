from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	"""Модель профиля пользователя.

	Атрибуты:
			user (OneToOneField): Связь с моделью User
			image (ImageField): Поле для загрузки изображения профиля

	Методы:
			__str__(): Возвращает строковое представление профиля пользователя
			save(): Переопределяет метод сохранения, чтобы изменить размер изображения
	"""

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		"""Возвращает строковое представление профиля пользователя."""
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		"""Сохраняет профиль и изменяет размер изображения, если оно слишком большое.

		Аргументы:
				*args: Позиционные аргументы.
				**kwargs: Именованные аргументы.
		"""
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
