from django.urls import path
from core import views
urlpatterns = [
    path("", views.home, name="home"),
    path("health/", views.health_check),
    path("about/", views.about),
    path("status/", views.status),
    path("info/", views.info),
    path("time/", views.time),
    path("metrics/", views.metrics),
    path("version/", views.version),
]