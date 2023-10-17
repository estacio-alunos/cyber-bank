from django.shortcuts import render


def hello(request):
    return render(
        request,
        'setup/index.html',
        {
            'context': 'Hello World!'
        }
    )
