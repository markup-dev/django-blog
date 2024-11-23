"""
ASGI конфигурация для проекта DjangoBlog.

Этот файл предоставляет ASGI вызываемый объект в качестве переменной уровня модуля с именем ``application``.

Для получения дополнительной информации об этом файле, смотрите:
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Установка переменной окружения для настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoBlog.settings')

# Получение ASGI приложения
application = get_asgi_application()
