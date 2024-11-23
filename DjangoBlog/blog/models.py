from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	"""Модель, представляющая пост блога.

	Атрибуты:
			title (str): Заголовок поста.
			content (str): Содержимое поста.
			date_posted (datetime): Дата и время публикации поста.
			author (User): Автор поста, связанный с моделью User.

	Методы:
			__str__(): Возвращает строковое представление заголовка поста.
			get_absolute_url(): Возвращает URL для доступа к конкретному посту.
	"""
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Возвращает строковое представление объекта Post."""
		return self.title

	def get_absolute_url(self):
		"""Возвращает URL для доступа к конкретному посту.

		Возвращает:
				str: URL для отображения деталей поста.
		"""
		return reverse('post-detail', kwargs={'pk': self.pk})
