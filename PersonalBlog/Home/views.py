from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'Carlos Alexis',
		'title': 'Mi Blog Personal',
		'content': 'Mi nombre es Carlos pero me conocen como Zerafin, se bienvenido',	
		'content': 'Me gustan los Videojuegos y leer Manga',
		'date_posted': '30 de Agosto del 2019',	
	}
]


def index(request):
	context = {
		'posts': posts
		}
    return render(request, 'Home/templates.html', context)
