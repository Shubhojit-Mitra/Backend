from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

# https://dev.to/koladev/building-a-fullstack-application-with-django-django-rest-nextjs-3e26
# https://blog.logrocket.com/how-and-why-you-should-use-next-js-django/

def hello(request):
    return JsonResponse({'message':'Hello world'})