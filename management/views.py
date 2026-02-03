import json
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.core import serializers
import orjson

from models.users import User

def serialize_user(user):
    data = {}
    for field in user._meta.fields:
        value = getattr(user, field.name)
        if isinstance(value, bytes) and field.name == 'is_deleted':
            value = bool(value[0])
        elif hasattr(value, 'strftime'):
            value = value.strftime('%Y-%m-%d %H:%M:%S')
        data[field.name] = value
    return data

# Create your views here.


@require_GET
def index(request):
    return HttpResponse("123")

@require_http_methods(["GET"])
def getUser(request):
    # User(name="test", type="admin").save()
    user = User.objects.get(id=7)
    data = orjson.dumps(serialize_user(user))
    return HttpResponse(data)
    # return JsonResponse(user, safe=False)