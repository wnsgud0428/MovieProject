from django.contrib import admin

from . import models
# Register your models here.

@admin.register(models.MovieModel)
class MovieAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("title","director","keyword")}
        ),

    )