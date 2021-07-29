from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    """List Admin Definition"""

    list_display = ("__str__", "count_rooms")

    filter_horizontal = ("rooms",)

    search_fields = ("name",)
