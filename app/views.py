from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def movie_page(request):
    return render(request, "movie-list.html")


def shrek_detail(request):
    return render(request, "shrek.html")


def lion_king_detail(request):
    return render(request, "lion_king.html")
