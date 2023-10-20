import json
from django.http.response import HttpResponse


def hello(http: any):
    return HttpResponse(json.dumps({'context': 'Hello World!'}), content_type="application/json")
