from django.http import JsonResponse
from datetime import datetime


def home(request):
    return JsonResponse({
        "message": "Django CI/CD is running successfully!",
        "welcome": "Hello, welcome to the Django CI/CD pipeline."
    })


def health_check(request):
    return JsonResponse({
        "status": "healthy",
        "message": "The application is running smoothly."
    })


def about(request):
    return JsonResponse({
        "project": "Django CI/CD Pipeline",
        "version": "1.0.0",
        "developer": "Prabesh",
        "framework": "Django"
    })


def info(request):
    return JsonResponse({
        "python_version": "3.x",
        "framework": "Django",
        "environment": "Development"
    })


def time(request):
    return JsonResponse({
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


def status(request):
    return JsonResponse({
        "application": "Running",
        "database": "Connected",
        "server": "Healthy"
    })