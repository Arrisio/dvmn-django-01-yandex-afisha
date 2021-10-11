from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    place = models.ForeignKey(
        Place, related_name="images", verbose_name="Место", on_delete=models.CASCADE
    )
    image = models.ImageField(verbose_name="Картинка")
    position = models.IntegerField(default=0)

    class Meta:
        ordering = [
            "position",
        ]
