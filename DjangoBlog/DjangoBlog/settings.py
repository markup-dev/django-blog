"""
Настройки Django для проекта DjangoBlog.

Этот файл был сгенерирован с помощью команды 'django-admin startproject' с использованием Django 5.1.3.

Для получения дополнительной информации об этом файле, смотрите:
https://docs.djangoproject.com/en/5.1/topics/settings/

Для полного списка настроек и их значений, смотрите:
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Построение путей внутри проекта, например: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Быстрая настройка разработки - не подходит для продакшн
# Смотрите: https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# ВНИМАНИЕ БЕЗОПАСНОСТИ: держите секретный ключ в секрете в продакшне!
SECRET_KEY = 'django-insecure-4_*cx%a4!8@#&(rz%hsw902(9tp-i)323p(i&@$2-7c%9u$if_'

# ВНИМАНИЕ БЕЗОПАСНОСТИ: не запускайте с включенной отладкой в продакшне!
DEBUG = True

ALLOWED_HOSTS = []

# Определение приложений
INSTALLED_APPS = [
	'blog.apps.BlogConfig',
	'users.apps.UsersConfig',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'crispy_forms',
	'crispy_bootstrap4',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoBlog.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'DjangoBlog.wsgi.application'

# Настройки базы данных
# Смотрите: https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',  # Использование SQLite в качестве базы данных
		'NAME': BASE_DIR / 'db.sqlite3',  # Имя файла базы данных
	}
}

# Проверка паролей
# Смотрите: https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

# Интернационализация
# Смотрите: https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'  # Код языка по умолчанию

TIME_ZONE = 'UTC'  # Часовой пояс по умолчанию

USE_I18N = True  # Включение интернационализации

USE_TZ = True  # Включение поддержки временных зон

# Статические файлы (CSS, JavaScript, изображения)
# Смотрите: https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'  # URL для статических файлов
MEDIA_URL = '/media/'  # URL для медиафайлов

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Папка для загружаемых медиафайлов

CRISPY_TEMPLATE_PACK = 'bootstrap4'  # Шаблон для crispy-forms

# Тип поля первичного ключа по умолчанию
# Смотрите: https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'blog-home'  # URL перенаправления после входа в систему
LOGIN_URL = 'login'  # URL для страницы входа в систему
