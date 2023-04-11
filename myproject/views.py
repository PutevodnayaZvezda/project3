from django.http import HttpResponse

def home(request):
    return HttpResponse("http://localhost:8000/tasks")
