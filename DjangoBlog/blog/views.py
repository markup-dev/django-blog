from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)

from .models import Post


def home(request):
	"""Отображение главной страницы со всеми постами.

	Аргументы:
			request (HttpRequest): Объект запроса от клиента.

	Возвращает:
			HttpResponse: Отвечает HTML-шаблоном главной страницы с контекстом всех постов.
	"""
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


class PostListView(ListView):
	"""Класс представления для отображения всех постов.

	Атрибуты:
			model (Post): Модель, используемая для получения данных
			template_name (str): Шаблон для отображения списка постов
			context_object_name (str): Имя переменной контекста для списка постов
			ordering (list): Порядок сортировки постов по дате публикации
			paginate_by (int): Количество постов на странице
	"""
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5


class UserPostListView(ListView):
	"""Класс представления для отображения постов конкретного пользователя.

	Атрибуты:
			model (Post): Модель, используемая для получения данных
			template_name (str): Шаблон для отображения списка постов пользователя
			context_object_name (str): Имя переменной контекста для списка постов пользователя
			paginate_by (int): Количество постов на странице

	Методы:
			get_queryset(): Возвращает набор запросов для получения постов текущего пользователя.
	"""
	model = Post
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		"""Возвращает посты, написанные указанным пользователем.

		Возвращает:
				QuerySet: Набор запросов с постами конкретного автора, отсортированными по дате публикации.
		"""
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
	"""Класс представления для отображения деталей одного поста."""
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	"""Класс представления для создания нового поста.

	Атрибуты:
			model (Post): Модель, используемая для создания нового объекта
			fields (list): Поля формы для создания нового поста

	Методы:
			form_valid(form): Устанавливает текущего пользователя как автора перед сохранением формы.
	"""
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		"""Устанавливает текущего пользователя как автора перед сохранением.

		Аргументы:
				form (Form): Форма с данными нового поста.

		Возвращает:
				HttpResponse: Ответ после успешного сохранения формы.
		"""
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	"""Класс представления для обновления существующего поста.

	Атрибуты:
			model (Post): Модель, используемая для обновления объекта
			fields (list): Поля формы для обновления существующего поста

	Методы:
			form_valid(form): Устанавливает текущего пользователя как автора перед сохранением формы
			test_func(): Проверяет, является ли текущий пользователь автором поста
	"""
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		"""Устанавливает текущего пользователя как автора перед сохранением.

		Аргументы:
				form (Form): Форма с данными обновленного поста.

		Возвращает:
				HttpResponse: Ответ после успешного сохранения формы.
		"""
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		"""Проверяет, является ли текущий пользователь автором поста.

		Возвращает:
				bool: True если пользователь является автором; иначе False.
		"""
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	"""Класс представления для удаления существующего поста.

	Атрибуты:
			model (Post): Модель, используемая для удаления объекта
			success_url (str): URL перенаправления после успешного удаления

	Методы:
			test_func(): Проверяет, является ли текущий пользователь автором поста.
	"""
	model = Post
	success_url = '/'

	def test_func(self):
		"""Проверяет, является ли текущий пользователь автором поста.

		Возвращает:
				bool: True если пользователь является автором; иначе False.
		"""
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
	"""Отображение страницы «О нас» блога.

	Аргументы:
			request (HttpRequest): Объект запроса от клиента.

	Возвращает:
			HttpResponse: Ответ с HTML-шаблоном страницы «О нас».
	"""
	return render(request, 'blog/about.html', {'title': 'О клубе Python Monolith'})
