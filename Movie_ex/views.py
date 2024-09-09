from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from rest_framework.generics import get_object_or_404

from Movie_ex.models import Movie, Actor


@user_passes_test(lambda user: user.is_staff)
def list_movies(request):
    movie_data = Movie.objects.all()
    return render(request, 'list_movies.html', {'movie_data': movie_data})


@user_passes_test(lambda user: user.is_staff)
def film_detail(request, movie_id):
    movie = Movie.objects.filter(pk=movie_id).first()
    title = movie.title
    actors = movie.actors.all()
    return render(request, 'film_detail.html', {'movie': movie, 'title': title, 'actors': actors})