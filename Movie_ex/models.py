from django.db import models
from django.db import models
from datetime import date

from django.urls import reverse

class Actor(models.Model):
    """Актеры"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актеры"
        verbose_name_plural = "Актеры"


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"




