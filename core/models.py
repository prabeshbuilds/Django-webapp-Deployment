from django.db import models


class Project(models.Model):
    ENVIRONMENT_CHOICES = [
        ("Development", "Development"),
        ("Staging", "Staging"),
        ("Production", "Production"),
    ]

    STATUS_CHOICES = [
        ("Running", "Running"),
        ("Stopped", "Stopped"),
        ("Failed", "Failed"),
        ("Maintenance", "Maintenance"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    version = models.CharField(max_length=20)
    environment = models.CharField(
        max_length=20,
        choices=ENVIRONMENT_CHOICES,
        default="Development",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Running",
    )
    repository = models.URLField(blank=True)
    deployed_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name