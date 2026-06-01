from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "🚀 Django CI/CD is running from scratch;;;!"
    })