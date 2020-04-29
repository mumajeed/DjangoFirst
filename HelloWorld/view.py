import textwrap

from django.http import HttpResponse


def printres(request):
    return HttpResponse(textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Welcome to home page </h1>
                <a href="http://127.0.0.1:8000/test">link</a>
            </body>
            </html>
        '''))
    return HttpResponse(request)


def to_do(request):
    return HttpResponse(textwrap.dedent('''\
            <html>
            <head>
                <title>To Do App</title>
            </head>
            <body>
                <h1>To Do App</h1>
                <p>Make your entries</p>
            </body>
            </html>
        '''))
    return HttpResponse(request)
    return print("Please Login")

