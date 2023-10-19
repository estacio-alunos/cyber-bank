from django.http import JsonResponse


def hello(request):
    return JsonResponse({'message': 'hello world!'}, status=200)
