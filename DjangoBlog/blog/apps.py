from django.apps import AppConfig


class BlogConfig(AppConfig):
	"""Конфигурация приложения Blog.

	Атрибуты:
			default_auto_field (str): Поле по умолчанию для автоматического создания идентификаторов.
			name (str): Имя приложения.
	"""
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'blog'
