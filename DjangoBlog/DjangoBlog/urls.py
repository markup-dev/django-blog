"""
Конфигурация URL для проекта DjangoBlog.

Список `urlpatterns` маршрутизирует URL-адреса к представлениям.
Для получения дополнительной информации смотрите:
https://docs.djangoproject.com/en/5.1/topics/http/urls/

Примеры:
Функциональные представления:
    1. Добавьте импорт: from my_app import views
    2. Добавьте URL в urlpatterns: path('', views.home, name='home')
Классовые представления:
    1. Добавьте импорт: from other_app.views import Home
    2. Добавьте URL в urlpatterns: path('', Home.as_view(), name='home')
Включение другого URLconf:
    1. Импортируйте функцию include: from django.urls import include, path
    2. Добавьте URL в urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
	path('admin/', admin.site.urls),  # Административная панель
	path('register/', user_views.register, name='register'),  # Регистрация пользователя
	path('profile/', user_views.profile, name='profile'),  # Профиль пользователя
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Вход пользователя
	path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
	# Выход пользователя
	path('', include('blog.urls')),  # Включение маршрутов блога
]

# Обработка медиафайлов в режиме отладки (DEBUG)
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
