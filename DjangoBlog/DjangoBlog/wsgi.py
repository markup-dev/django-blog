"""
WSGI конфигурация для проекта DjangoBlog.

Этот файл предоставляет WSGI вызываемый объект в качестве переменной уровня модуля с именем ``application``.

Для получения дополнительной информации об этом файле, смотрите:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Установка переменной окружения для настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoBlog.settings')

# Получение WSGI приложения
application = get_wsgi_application()
