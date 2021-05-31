from django.contrib import admin

# Register your models here.
# #http://127.0.0.1:8000/admin/
# hoseong // 12 or 123

from . import models

@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "weight")}
        ),

    )

@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "weight")}
        ),

    )

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "weight")}
        ),

    )



