from django.apps import AppConfig


class UsersConfig(AppConfig):
	"""Конфигурация приложения Users.

	Атрибуты:
			name (str): Имя приложения.
	"""
	name = 'users'

	def ready(self):
		"""Импортирует сигналы приложения при его готовности."""
		import users.signals
