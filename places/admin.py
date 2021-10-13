from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html


from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image

    extra = 1
    readonly_fields = ["preview_image"]
    fields = ("image", "preview_image", "position")

    def preview_image(self, obj):
        return format_html(
            '<img src="{url}" style="max-height:200px;max-width:400px" />',
            url=obj.image.url,
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Image)
