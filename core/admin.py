from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "version",
        "environment",
        "status",
        "created_at",
    )

    list_filter = (
        "environment",
        "status",
    )

    search_fields = (
        "name",
        "version",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Project Information",
            {
                "fields": (
                    "name",
                    "description",
                    "version",
                )
            },
        ),
        (
            "Deployment",
            {
                "fields": (
                    "environment",
                    "status",
                    "repository",
                    "deployed_url",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )