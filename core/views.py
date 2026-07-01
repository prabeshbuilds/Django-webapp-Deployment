from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Django CI/CD is running successfullyyyyyy!",
        "welcome": "Hello, welcome to the Django CI/CD pipeline."
    })
