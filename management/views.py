from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST
# Create your views here.


@require_GET
def index(request):
    return HttpResponse("123")

@require_http_methods(["GET"])
def getUser(request):
    return HttpResponse("get user")