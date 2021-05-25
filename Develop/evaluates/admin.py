from django.contrib import admin

from . import models
# Register your models here.

@admin.register(models.Evaluate)
class EvalAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("user","keyword")}
        ),

    )