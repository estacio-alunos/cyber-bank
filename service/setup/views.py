from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods


@require_POST
def post(request) -> JsonResponse:
    return JsonResponse(data={'message': 'POST'}, status=200)


@require_GET
def get(request) -> JsonResponse:
    data = {'message': 'GET'}
    return JsonResponse(data=data, status=201)


@require_http_methods(['GET', 'POST'])
def post_get(request) -> JsonResponse:
    return JsonResponse(data={'message': 'GET ou POST'}, status=200)
