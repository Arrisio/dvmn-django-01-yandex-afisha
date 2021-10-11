from django.db import models

# Create your models here.
from yandex_afisha import settings


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description_short = models.CharField(max_length=255, verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    place = models.ForeignKey(
        Place, related_name="images", verbose_name="Место", on_delete=models.CASCADE
    )
    image = models.ImageField(verbose_name="Картинка")
    position = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.place})"

    class Meta:
        ordering = [
            "position",
        ]
