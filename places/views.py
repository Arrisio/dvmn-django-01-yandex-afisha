import json
from django.shortcuts import render
from .models import Place


# def compile_geojson_from_place(place) -> dict:
#     return {
#         "type": "Feature",
#         "geometry": {"type": "Point", "coordinates": [place.lng, place.lat]},
#         "properties": {
#             "title": place.title,
#             "placeId": place.id,
#             "detailsUrl": {"data": json.dumps({
#                 "title": place.title,
#                 "imgs": [img.image.url for img in place.images.all()],
#                 "description_short": place.description_short,
#                 "description_long": place.description_long,
#                 "coordinates": {"lng": str(place.lng), "lat": str(place.lat)},
#             })},
#         },
#     }


def show_index(request):
    # template = loader.get_template()
    # geojson = {
    #     "type": "FeatureCollection",
    #     "features": [
    #         compile_geojson_from_place(place)
    #         for place in Place.objects.prefetch_related("images").all()
    #     ],
    # }

    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [place.lng, place.lat]},
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json",
                },
            }
            for place in Place.objects.prefetch_related("images").all()
        ],
    }

    return render(request, "index.html", context={"geojson": geojson})
