from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	"""Создает профиль пользователя при создании нового пользователя.

	Аргументы:
			sender (Model): Модель, отправившая сигнал
			instance (User): Экземпляр созданного пользователя
			created (bool): Указывает, был ли создан новый экземпляр
			**kwargs: Дополнительные аргументы
	"""
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	"""Сохраняет профиль пользователя при сохранении экземпляра пользователя.

	Аргументы:
			sender (Model): Модель, отправившая сигнал
			instance (User): Экземпляр пользователя
			**kwargs: Дополнительные аргументы
	"""
	instance.profile.save()
