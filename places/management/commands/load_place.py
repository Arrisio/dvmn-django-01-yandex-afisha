import os

import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Image, Place


class Command(BaseCommand):
    help = "Load place to website"

    def add_arguments(self, parser):
        parser.add_argument("url", type=str)

    def handle(self, *args, **options):
        response = requests.get(options["url"])
        response.raise_for_status()
        place_description = response.json()

        place, created = Place.objects.update_or_create(
            title=place_description["title"],
            defaults={
                "title": place_description["title"],
                "description_short": place_description["description_short"],
                "description_long": place_description["description_long"],
                "lng": place_description["coordinates"]["lng"],
                "lat": place_description["coordinates"]["lat"],
            },
        )

        for position, img_link in enumerate(place_description["imgs"]):
            image, created = Image.objects.get_or_create(
                place=place,
                position=position,
            )
            img = requests.get(img_link)
            response.raise_for_status()

            image.image.save(
                os.path.basename(img.url), ContentFile(img.content), save=True
            )
