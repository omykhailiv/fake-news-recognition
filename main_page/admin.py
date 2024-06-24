from django.contrib import admin
from .models import CheckedTitles


class CheckedTitlesAdmin(admin.ModelAdmin):
    list_display = ["title", "prediction", "score"]
    fieldsets = [
        (None, {"fields": ["title", "prediction", "score"]})
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["title", "prediction", "score"],
            },
        ),
    ]
    search_fields = ["title", "prediction", "score"]
    ordering = ["title", "prediction", "score"]
    filter_horizontal = []

# Реєстрація моделі та класу адміністратора
admin.site.register(CheckedTitles, CheckedTitlesAdmin)
